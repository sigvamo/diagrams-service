var express = require("express");
var app = express();
const { exec } = require('child_process');
const crypto = require('crypto');
const fs = require('fs');
require('dotenv').config();
const AWS = require('aws-sdk');
const bodyParser = require('body-parser');

app.use(bodyParser.json());
app.use(express.json());



const sm = new AWS.SecretsManager({});

sm.getSecretValue({SecretId: "diagrams-service"}, function(err, data) {
	    if (err) {
		   console.log('Cant read AWS Secrets Manager secret diagrams-service');
		   throw err;
            } else {    

     if ('SecretString' in data) {
        secret = JSON.parse(data.SecretString); 
   } else {
	let buff = new Buffer(data.SecretBinary, 'base64');
	decodedBinarySecret = buff.toString('ascii');
   }}


const ddb = new AWS.DynamoDB({apiVersion: '2012-08-10', 
	                      region: process.env.AWS_REGION
	                     });


const s3 = new AWS.S3({});

const imports = fs.readFileSync("imports.py");

// Create S3 bucket
const s3params = {
	    Bucket: secret.AWS_S3_BUCKET_NAME,
	    CreateBucketConfiguration: { LocationConstraint: process.env.AWS_REGION }
              }


s3.createBucket(s3params, function(err, data) {
	   if (err && err.statusCode == 409){
		   console.log(`Bucket ${secret.AWS_S3_BUCKET_NAME} exists.`);
	      } else if (data) {
	           console.log('Bucket created successfully', data.Location);
              } else {
                   console.log('Failed to create bucket', secret.AWS_S3_BUCKET_NAME, err.message);
              }
});


// Create DynamoDB table
const ddbparams = {
	  AttributeDefinitions: [
		      {
			            AttributeName: 'HASH',
			            AttributeType: 'S'
			          }
		    ],
	  KeySchema: [
		      {
			            AttributeName: 'HASH',
			            KeyType: 'HASH'
			          }
		    ],
	  TableName: secret.AWS_DDB_TABLE,
	  BillingMode: 'PAY_PER_REQUEST',
	  StreamSpecification: {
		      StreamEnabled: false
		    },
          Tags: [
		    {
			          Key: 'app',
			          Value: 'diagrams'
			        }]
};

ddb.describeTable({ TableName: secret.AWS_DDB_TABLE }, function(err, data) {
	  if (err) {
	     console.log('Cannot describe DynamoDB table, trying to create');
             ddb.createTable(ddbparams, function(err, data) {
		   if (err)  {
			   console.log("Error createing DynamoDB table", secret.AWS_DDB_TABLE, err);
		   } else {
			  console.log("DynamoDB table created", data);
		   }
	     });


	  } else     console.log('DynamoDB table exists', data);
});



const uploadFileS3 = async function (fileName) {

	const file = fs.readFileSync(`${process.env.TEMP_FILES_LOCATION}/${fileName}`);

	const params = {
	         Bucket: secret.AWS_S3_BUCKET_NAME,
	         Key: fileName,
	         Body: file,
		 ContentType: "image/png"
	};
	
	try {
		data = await s3.upload(params).promise();
	} catch(err) {
         	console.log(`Error uploading file ${err}`);
		return "null"
	}

	console.log(`File uploaded successfully. ${data.Location}`);
	return data.Location

};


const putItemDDB = async function (hash) {
   
    try {
      let result = await ddb.putItem({
                      TableName: secret.AWS_DDB_TABLE,
                      Item: {
                                'HASH' : {S: hash},
                                'STAT' : {S: 'INPROGRESS'}
                      }}).promise();
    }
    catch(err)
    {
      console.log("Error putting into dynamoDB table", err);
      return 1
    }
   
    return 0

}


const deleteItemDDB = async function (hash) {

            let result = await ddb.deleteItem({
			TableName: secret.AWS_DDB_TABLE,
	                Key: {
	                   'HASH' : {S: hash}
	                }}).promise();
	    return 0

}


const updateItemDDB = async function (hash, val, URL) {

    try {
      let result = await ddb.updateItem({
	             TableName: secret.AWS_DDB_TABLE,
                     Key: { 
			     'HASH' : {"S": hash}
		           },
	             UpdateExpression: "set STAT = :val1, S3URL = :val2",
	             ExpressionAttributeValues: {
			             ":val1": {"S": val},
		                     ":val2": {"S": URL}
                     }}).promise();
		     }
	             catch(err)
		     {
		          console.log("Error updating dynamoDB table", err);
		          return 1
		     }
      return 0
}


app.post("/create", async (req, res, next) => {
    
    let request_hash = generate_hash(req.body.text);
 
    let row = await ddb.getItem({TableName: secret.AWS_DDB_TABLE,
	                         ConsistentRead: true,
	                         Key: {
				   'HASH' : {"S": request_hash}
			        }}).promise();


    if (row.Item) {
         if (row.Item.STAT.S === "SUCCESS") {
	        res.status(200).json({"status": row.Item.STAT.S, "url": row.Item.S3URL.S});
         } else if (row.Item.STAT.S === "INPROGRESS") {
		res.status(200).json({"status": row.Item.STAT.S});
         } else { 
	        post_diagram(req, res, request_hash);
         }
    } else {
	 post_diagram(req, res, request_hash);
    }

});


app.get('/get', async function(req, res) {

   let request_hash = req.query.hash

   let row = await ddb.getItem({TableName: secret.AWS_DDB_TABLE,
                                    Key: {
			                   'HASH' : {"S": request_hash}
			                 }}).promise();

   if (row.Item) {
       res.status(200).json({"status": row.Item.STAT.S, "url": (row.Item.S3URL) ? row.Item.S3URL.S : "none"});
   } else {
       res.status(200).json({"status": "NO_DATA_FOUND"});
   }

});


app.get('/ping', async function(req, res) {

  res.status(200).json({"status": "SUCCESS"});

});


const generate_hash = function (text) {
   return crypto.createHash('md5').update(text).digest("hex")
}

const post_diagram = function (req, res, hash) {

   let request_hash = hash;
   
   putItemDDB(request_hash);

   generate_py(request_hash, req.body.text);
   
   exec(`python3 ${process.env.TEMP_FILES_LOCATION}/${request_hash}.py`, async (error, stdout, stderr) => {
	    console.log(error, stdout, stderr)
	if (error) {
	    res.status(400).json({"status": "ERROR"})
	    updateItemDDB(request_hash, "ERROR", "none");
	} else {
	    res.status(200).json({"status": "INPROGRESS", "hash": request_hash});
	    try {
	        let s3URL = await uploadFileS3(`${request_hash}.png`);
	        updateItemDDB(request_hash, "SUCCESS", `${secret.AWS_CFD_DOMAIN}/${request_hash}.png`);
	    } catch (err) {
		console.log(`Error uploading file to S3 bucket ${secret.AWS_S3_BUCKET_NAME} in region ${process.env.AWS_REGION}`, err);
                updateItemDDB(request_hash, "ERROR", "none");
            } finally {
         	fs.unlink(`${process.env.TEMP_FILES_LOCATION}/${request_hash}.py`, () => {});
	        fs.unlink(`${process.env.TEMP_FILES_LOCATION}/${request_hash}.png`, () => {});
            }
	}
   });
   
}

const generate_py = function (hash, dtext) {

  let body = `
from diagrams import Diagram
${imports}

with Diagram("", show=False, filename="${process.env.TEMP_FILES_LOCATION}/${hash}"):
   ${dtext}
`

  fs.writeFile(`${process.env.TEMP_FILES_LOCATION}/${hash}.py`, body, function (err) {
	    if (err) return console.log(err);
  });

}



app.listen(3000, () => {
	 console.log("Server running on port 3000");
});



});
