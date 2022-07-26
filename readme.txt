# 

docker build -t diagrams:3 .
docker run -p 3000:3000 -e AWS_REGION="eu-central-1" diagrams:3
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 457814457916.dkr.ecr.eu-central-1.amazonaws.com
docker images
docker tag diagrams:3 457814457916.dkr.ecr.eu-central-1.amazonaws.com/diagrams-service
docker images
docker push 457814457916.dkr.ecr.eu-central-1.amazonaws.com/diagrams-service:latest

