from diagrams.aws.analytics import Analytics
from diagrams.aws.analytics import Athena
from diagrams.aws.analytics import CloudsearchSearchDocuments
from diagrams.aws.analytics import Cloudsearch
from diagrams.aws.analytics import DataLakeResource
from diagrams.aws.analytics import DataPipeline
from diagrams.aws.analytics import ElasticsearchService, ES
from diagrams.aws.analytics import EMRCluster
from diagrams.aws.analytics import EMREngineMaprM3
from diagrams.aws.analytics import EMREngineMaprM5
from diagrams.aws.analytics import EMREngineMaprM7
from diagrams.aws.analytics import EMREngine
from diagrams.aws.analytics import EMRHdfsCluster
from diagrams.aws.analytics import EMR
from diagrams.aws.analytics import GlueCrawlers
from diagrams.aws.analytics import GlueDataCatalog
from diagrams.aws.analytics import Glue
from diagrams.aws.analytics import KinesisDataAnalytics
from diagrams.aws.analytics import KinesisDataFirehose
from diagrams.aws.analytics import KinesisDataStreams
from diagrams.aws.analytics import KinesisVideoStreams
from diagrams.aws.analytics import Kinesis
from diagrams.aws.analytics import LakeFormation
from diagrams.aws.analytics import ManagedStreamingForKafka
from diagrams.aws.analytics import Quicksight
from diagrams.aws.analytics import RedshiftDenseComputeNode
from diagrams.aws.analytics import RedshiftDenseStorageNode
from diagrams.aws.analytics import Redshift

from diagrams.aws.ar import ArVr
from diagrams.aws.ar import Sumerian

from diagrams.aws.blockchain import BlockchainResource
from diagrams.aws.blockchain import Blockchain
from diagrams.aws.blockchain import ManagedBlockchain
from diagrams.aws.blockchain import QuantumLedgerDatabaseQldb, QLDB

from diagrams.aws.business import AlexaForBusiness, A4B
from diagrams.aws.business import BusinessApplications
from diagrams.aws.business import Chime
from diagrams.aws.business import Workmail

from diagrams.aws.compute import ApplicationAutoScaling, AutoScaling
from diagrams.aws.compute import Batch
from diagrams.aws.compute import ComputeOptimizer
from diagrams.aws.compute import Compute
from diagrams.aws.compute import EC2Ami, AMI
from diagrams.aws.compute import EC2AutoScaling
from diagrams.aws.compute import EC2ContainerRegistryImage
from diagrams.aws.compute import EC2ContainerRegistryRegistry
from diagrams.aws.compute import EC2ContainerRegistry, ECR
from diagrams.aws.compute import EC2ElasticIpAddress
from diagrams.aws.compute import EC2ImageBuilder
from diagrams.aws.compute import EC2Instance
from diagrams.aws.compute import EC2Instances
from diagrams.aws.compute import EC2Rescue
from diagrams.aws.compute import EC2SpotInstance
from diagrams.aws.compute import EC2
from diagrams.aws.compute import ElasticBeanstalkApplication
from diagrams.aws.compute import ElasticBeanstalkDeployment
from diagrams.aws.compute import ElasticBeanstalk, EB
from diagrams.aws.compute import ElasticContainerServiceContainer
from diagrams.aws.compute import ElasticContainerServiceService
from diagrams.aws.compute import ElasticContainerService, ECS
from diagrams.aws.compute import ElasticKubernetesService, EKS
from diagrams.aws.compute import Fargate
from diagrams.aws.compute import LambdaFunction
from diagrams.aws.compute import Lambda
from diagrams.aws.compute import Lightsail
from diagrams.aws.compute import LocalZones
from diagrams.aws.compute import Outposts
from diagrams.aws.compute import ServerlessApplicationRepository, SAR
from diagrams.aws.compute import ThinkboxDeadline
from diagrams.aws.compute import ThinkboxDraft
from diagrams.aws.compute import ThinkboxFrost
from diagrams.aws.compute import ThinkboxKrakatoa
from diagrams.aws.compute import ThinkboxSequoia
from diagrams.aws.compute import ThinkboxStoke
from diagrams.aws.compute import ThinkboxXmesh
from diagrams.aws.compute import VmwareCloudOnAWS
from diagrams.aws.compute import Wavelength

from diagrams.aws.cost import Budgets
from diagrams.aws.cost import CostAndUsageReport
from diagrams.aws.cost import CostExplorer
from diagrams.aws.cost import CostManagement
from diagrams.aws.cost import ReservedInstanceReporting
from diagrams.aws.cost import SavingsPlans

from diagrams.aws.database import AuroraInstance
from diagrams.aws.database import Aurora
from diagrams.aws.database import DatabaseMigrationServiceDatabaseMigrationWorkflow
from diagrams.aws.database import DatabaseMigrationService, DMS
from diagrams.aws.database import Database, DB
from diagrams.aws.database import DocumentdbMongodbCompatibility, DocumentDB
from diagrams.aws.database import DynamodbAttribute
from diagrams.aws.database import DynamodbAttributes
from diagrams.aws.database import DynamodbDax, DAX
from diagrams.aws.database import DynamodbGlobalSecondaryIndex, DynamodbGSI
from diagrams.aws.database import DynamodbItem
from diagrams.aws.database import DynamodbItems
from diagrams.aws.database import DynamodbTable
from diagrams.aws.database import Dynamodb, DDB
from diagrams.aws.database import ElasticacheCacheNode
from diagrams.aws.database import ElasticacheForMemcached
from diagrams.aws.database import ElasticacheForRedis
from diagrams.aws.database import Elasticache, ElastiCache
from diagrams.aws.database import KeyspacesManagedApacheCassandraService
from diagrams.aws.database import Neptune
from diagrams.aws.database import QuantumLedgerDatabaseQldb, QLDB
from diagrams.aws.database import RDSInstance
from diagrams.aws.database import RDSMariadbInstance
from diagrams.aws.database import RDSMysqlInstance
from diagrams.aws.database import RDSOnVmware
from diagrams.aws.database import RDSOracleInstance
from diagrams.aws.database import RDSPostgresqlInstance
from diagrams.aws.database import RDSSqlServerInstance
from diagrams.aws.database import RDS
from diagrams.aws.database import RedshiftDenseComputeNode
from diagrams.aws.database import RedshiftDenseStorageNode
from diagrams.aws.database import Redshift
from diagrams.aws.database import Timestream

from diagrams.aws.devtools import CloudDevelopmentKit
from diagrams.aws.devtools import Cloud9Resource
from diagrams.aws.devtools import Cloud9
from diagrams.aws.devtools import Codebuild
from diagrams.aws.devtools import Codecommit
from diagrams.aws.devtools import Codedeploy
from diagrams.aws.devtools import Codepipeline
from diagrams.aws.devtools import Codestar
from diagrams.aws.devtools import CommandLineInterface, CLI
from diagrams.aws.devtools import DeveloperTools, DevTools
from diagrams.aws.devtools import ToolsAndSdks
from diagrams.aws.devtools import XRay

from diagrams.aws.enablement import CustomerEnablement
from diagrams.aws.enablement import Iq
from diagrams.aws.enablement import ManagedServices
from diagrams.aws.enablement import ProfessionalServices
from diagrams.aws.enablement import Support

from diagrams.aws.enduser import Appstream20
from diagrams.aws.enduser import DesktopAndAppStreaming
from diagrams.aws.enduser import Workdocs
from diagrams.aws.enduser import Worklink
from diagrams.aws.enduser import Workspaces

from diagrams.aws.engagement import Connect
from diagrams.aws.engagement import CustomerEngagement
from diagrams.aws.engagement import Pinpoint
from diagrams.aws.engagement import SimpleEmailServiceSesEmail
from diagrams.aws.engagement import SimpleEmailServiceSes, SES

from diagrams.aws.game import GameTech
from diagrams.aws.game import Gamelift

from diagrams.aws.general import Client
from diagrams.aws.general import Disk
from diagrams.aws.general import Forums
from diagrams.aws.general import General
from diagrams.aws.general import GenericDatabase
from diagrams.aws.general import GenericFirewall
from diagrams.aws.general import GenericOfficeBuilding, OfficeBuilding
from diagrams.aws.general import GenericSamlToken
from diagrams.aws.general import GenericSDK
from diagrams.aws.general import InternetAlt1
from diagrams.aws.general import InternetAlt2
from diagrams.aws.general import InternetGateway
from diagrams.aws.general import Marketplace
from diagrams.aws.general import MobileClient
from diagrams.aws.general import Multimedia
from diagrams.aws.general import OfficeBuilding
from diagrams.aws.general import SamlToken
from diagrams.aws.general import SDK
from diagrams.aws.general import SslPadlock
from diagrams.aws.general import TapeStorage
from diagrams.aws.general import Toolkit
from diagrams.aws.general import TraditionalServer
from diagrams.aws.general import User
from diagrams.aws.general import Users

from diagrams.aws.integration import ApplicationIntegration
from diagrams.aws.integration import Appsync
from diagrams.aws.integration import ConsoleMobileApplication
from diagrams.aws.integration import EventResource
from diagrams.aws.integration import EventbridgeCustomEventBusResource
from diagrams.aws.integration import EventbridgeDefaultEventBusResource
from diagrams.aws.integration import EventbridgeSaasPartnerEventBusResource
from diagrams.aws.integration import Eventbridge
from diagrams.aws.integration import ExpressWorkflows
from diagrams.aws.integration import MQ
from diagrams.aws.integration import SimpleNotificationServiceSnsEmailNotification
from diagrams.aws.integration import SimpleNotificationServiceSnsHttpNotification
from diagrams.aws.integration import SimpleNotificationServiceSnsTopic
from diagrams.aws.integration import SimpleNotificationServiceSns, SNS
from diagrams.aws.integration import SimpleQueueServiceSqsMessage
from diagrams.aws.integration import SimpleQueueServiceSqsQueue
from diagrams.aws.integration import SimpleQueueServiceSqs, SQS
from diagrams.aws.integration import StepFunctions, SF

from diagrams.aws.iot import Freertos, FreeRTOS
from diagrams.aws.iot import InternetOfThings
from diagrams.aws.iot import Iot1Click
from diagrams.aws.iot import IotAction
from diagrams.aws.iot import IotActuator
from diagrams.aws.iot import IotAlexaEcho
from diagrams.aws.iot import IotAlexaEnabledDevice
from diagrams.aws.iot import IotAlexaSkill
from diagrams.aws.iot import IotAlexaVoiceService
from diagrams.aws.iot import IotAnalyticsChannel
from diagrams.aws.iot import IotAnalyticsDataSet
from diagrams.aws.iot import IotAnalyticsDataStore
from diagrams.aws.iot import IotAnalyticsNotebook
from diagrams.aws.iot import IotAnalyticsPipeline
from diagrams.aws.iot import IotAnalytics
from diagrams.aws.iot import IotBank
from diagrams.aws.iot import IotBicycle
from diagrams.aws.iot import IotButton
from diagrams.aws.iot import IotCamera
from diagrams.aws.iot import IotCar
from diagrams.aws.iot import IotCart
from diagrams.aws.iot import IotCertificate
from diagrams.aws.iot import IotCoffeePot
from diagrams.aws.iot import IotCore
from diagrams.aws.iot import IotDesiredState
from diagrams.aws.iot import IotDeviceDefender
from diagrams.aws.iot import IotDeviceGateway
from diagrams.aws.iot import IotDeviceManagement
from diagrams.aws.iot import IotDoorLock
from diagrams.aws.iot import IotEvents
from diagrams.aws.iot import IotFactory
from diagrams.aws.iot import IotFireTvStick
from diagrams.aws.iot import IotFireTv
from diagrams.aws.iot import IotGeneric
from diagrams.aws.iot import IotGreengrassConnector
from diagrams.aws.iot import IotGreengrass
from diagrams.aws.iot import IotHardwareBoard, IotBoard
from diagrams.aws.iot import IotHouse
from diagrams.aws.iot import IotHttp
from diagrams.aws.iot import IotHttp2
from diagrams.aws.iot import IotJobs
from diagrams.aws.iot import IotLambda
from diagrams.aws.iot import IotLightbulb
from diagrams.aws.iot import IotMedicalEmergency
from diagrams.aws.iot import IotMqtt
from diagrams.aws.iot import IotOverTheAirUpdate
from diagrams.aws.iot import IotPolicyEmergency
from diagrams.aws.iot import IotPolicy
from diagrams.aws.iot import IotReportedState
from diagrams.aws.iot import IotRule
from diagrams.aws.iot import IotSensor
from diagrams.aws.iot import IotServo
from diagrams.aws.iot import IotShadow
from diagrams.aws.iot import IotSimulator
from diagrams.aws.iot import IotSitewise
from diagrams.aws.iot import IotThermostat
from diagrams.aws.iot import IotThingsGraph
from diagrams.aws.iot import IotTopic
from diagrams.aws.iot import IotTravel
from diagrams.aws.iot import IotUtility
from diagrams.aws.iot import IotWindfarm

from diagrams.aws.management import AutoScaling
from diagrams.aws.management import Chatbot
from diagrams.aws.management import CloudformationChangeSet
from diagrams.aws.management import CloudformationStack
from diagrams.aws.management import CloudformationTemplate
from diagrams.aws.management import Cloudformation
from diagrams.aws.management import Cloudtrail
from diagrams.aws.management import CloudwatchAlarm
from diagrams.aws.management import CloudwatchEventEventBased
from diagrams.aws.management import CloudwatchEventTimeBased
from diagrams.aws.management import CloudwatchRule
from diagrams.aws.management import Cloudwatch
from diagrams.aws.management import Codeguru
from diagrams.aws.management import CommandLineInterface
from diagrams.aws.management import Config
from diagrams.aws.management import ControlTower
from diagrams.aws.management import LicenseManager
from diagrams.aws.management import ManagedServices
from diagrams.aws.management import ManagementAndGovernance
from diagrams.aws.management import ManagementConsole
from diagrams.aws.management import OpsworksApps
from diagrams.aws.management import OpsworksDeployments
from diagrams.aws.management import OpsworksInstances
from diagrams.aws.management import OpsworksLayers
from diagrams.aws.management import OpsworksMonitoring
from diagrams.aws.management import OpsworksPermissions
from diagrams.aws.management import OpsworksResources
from diagrams.aws.management import OpsworksStack
from diagrams.aws.management import Opsworks
from diagrams.aws.management import OrganizationsAccount
from diagrams.aws.management import OrganizationsOrganizationalUnit
from diagrams.aws.management import Organizations
from diagrams.aws.management import PersonalHealthDashboard
from diagrams.aws.management import ServiceCatalog
from diagrams.aws.management import SystemsManagerAutomation
from diagrams.aws.management import SystemsManagerDocuments
from diagrams.aws.management import SystemsManagerInventory
from diagrams.aws.management import SystemsManagerMaintenanceWindows
from diagrams.aws.management import SystemsManagerOpscenter
from diagrams.aws.management import SystemsManagerParameterStore, ParameterStore
from diagrams.aws.management import SystemsManagerPatchManager
from diagrams.aws.management import SystemsManagerRunCommand
from diagrams.aws.management import SystemsManagerStateManager
from diagrams.aws.management import SystemsManager, SSM
from diagrams.aws.management import TrustedAdvisorChecklistCost
from diagrams.aws.management import TrustedAdvisorChecklistFaultTolerant
from diagrams.aws.management import TrustedAdvisorChecklistPerformance
from diagrams.aws.management import TrustedAdvisorChecklistSecurity
from diagrams.aws.management import TrustedAdvisorChecklist
from diagrams.aws.management import TrustedAdvisor
from diagrams.aws.management import WellArchitectedTool

from diagrams.aws.media import ElasticTranscoder
from diagrams.aws.media import ElementalConductor
from diagrams.aws.media import ElementalDelta
from diagrams.aws.media import ElementalLive
from diagrams.aws.media import ElementalMediaconnect
from diagrams.aws.media import ElementalMediaconvert
from diagrams.aws.media import ElementalMedialive
from diagrams.aws.media import ElementalMediapackage
from diagrams.aws.media import ElementalMediastore
from diagrams.aws.media import ElementalMediatailor
from diagrams.aws.media import ElementalServer
from diagrams.aws.media import KinesisVideoStreams
from diagrams.aws.media import MediaServices

from diagrams.aws.migration import ApplicationDiscoveryService, ADS
from diagrams.aws.migration import CloudendureMigration, CEM
from diagrams.aws.migration import DatabaseMigrationService, DMS
from diagrams.aws.migration import DatasyncAgent
from diagrams.aws.migration import Datasync
from diagrams.aws.migration import MigrationAndTransfer, MAT
from diagrams.aws.migration import MigrationHub
from diagrams.aws.migration import ServerMigrationService, SMS
from diagrams.aws.migration import SnowballEdge
from diagrams.aws.migration import Snowball
from diagrams.aws.migration import Snowmobile
from diagrams.aws.migration import TransferForSftp

from diagrams.aws.ml import ApacheMxnetOnAWS
from diagrams.aws.ml import AugmentedAi
from diagrams.aws.ml import Comprehend
from diagrams.aws.ml import DeepLearningAmis
from diagrams.aws.ml import DeepLearningContainers, DLC
from diagrams.aws.ml import Deepcomposer
from diagrams.aws.ml import Deeplens
from diagrams.aws.ml import Deepracer
from diagrams.aws.ml import ElasticInference
from diagrams.aws.ml import Forecast
from diagrams.aws.ml import FraudDetector
from diagrams.aws.ml import Kendra
from diagrams.aws.ml import Lex
from diagrams.aws.ml import MachineLearning
from diagrams.aws.ml import Personalize
from diagrams.aws.ml import Polly
from diagrams.aws.ml import RekognitionImage
from diagrams.aws.ml import RekognitionVideo
from diagrams.aws.ml import Rekognition
from diagrams.aws.ml import SagemakerGroundTruth
from diagrams.aws.ml import SagemakerModel
from diagrams.aws.ml import SagemakerNotebook
from diagrams.aws.ml import SagemakerTrainingJob
from diagrams.aws.ml import Sagemaker
from diagrams.aws.ml import TensorflowOnAWS
from diagrams.aws.ml import Textract
from diagrams.aws.ml import Transcribe
from diagrams.aws.ml import Translate

from diagrams.aws.mobile import Amplify
from diagrams.aws.mobile import APIGatewayEndpoint
from diagrams.aws.mobile import APIGateway
from diagrams.aws.mobile import Appsync
from diagrams.aws.mobile import DeviceFarm
from diagrams.aws.mobile import Mobile
from diagrams.aws.mobile import Pinpoint

from diagrams.aws.network import APIGatewayEndpoint
from diagrams.aws.network import APIGateway
from diagrams.aws.network import AppMesh
from diagrams.aws.network import ClientVpn
from diagrams.aws.network import CloudMap
from diagrams.aws.network import CloudFrontDownloadDistribution
from diagrams.aws.network import CloudFrontEdgeLocation
from diagrams.aws.network import CloudFrontStreamingDistribution
from diagrams.aws.network import CloudFront, CF
from diagrams.aws.network import DirectConnect
from diagrams.aws.network import ElasticLoadBalancing, ELB
from diagrams.aws.network import ElbApplicationLoadBalancer, ALB
from diagrams.aws.network import ElbClassicLoadBalancer, CLB
from diagrams.aws.network import ElbNetworkLoadBalancer, NLB
from diagrams.aws.network import Endpoint
from diagrams.aws.network import GlobalAccelerator, GAX
from diagrams.aws.network import InternetGateway
from diagrams.aws.network import Nacl
from diagrams.aws.network import NATGateway
from diagrams.aws.network import NetworkingAndContentDelivery
from diagrams.aws.network import PrivateSubnet
from diagrams.aws.network import Privatelink
from diagrams.aws.network import PublicSubnet
from diagrams.aws.network import Route53HostedZone
from diagrams.aws.network import Route53
from diagrams.aws.network import RouteTable
from diagrams.aws.network import SiteToSiteVpn
from diagrams.aws.network import TransitGateway
from diagrams.aws.network import VPCCustomerGateway
from diagrams.aws.network import VPCElasticNetworkAdapter
from diagrams.aws.network import VPCElasticNetworkInterface
from diagrams.aws.network import VPCFlowLogs
from diagrams.aws.network import VPCPeering
from diagrams.aws.network import VPCRouter
from diagrams.aws.network import VPCTrafficMirroring
from diagrams.aws.network import VPC
from diagrams.aws.network import VpnConnection
from diagrams.aws.network import VpnGateway

from diagrams.aws.quantum import Braket
from diagrams.aws.quantum import QuantumTechnologies

from diagrams.aws.robotics import RobomakerCloudExtensionRos
from diagrams.aws.robotics import RobomakerDevelopmentEnvironment
from diagrams.aws.robotics import RobomakerFleetManagement
from diagrams.aws.robotics import RobomakerSimulator
from diagrams.aws.robotics import Robomaker
from diagrams.aws.robotics import Robotics

from diagrams.aws.satellite import GroundStation
from diagrams.aws.satellite import Satellite

from diagrams.aws.security import AdConnector
from diagrams.aws.security import Artifact
from diagrams.aws.security import CertificateAuthority
from diagrams.aws.security import CertificateManager, ACM
from diagrams.aws.security import CloudDirectory
from diagrams.aws.security import Cloudhsm, CloudHSM
from diagrams.aws.security import Cognito
from diagrams.aws.security import Detective
from diagrams.aws.security import DirectoryService, DS
from diagrams.aws.security import FirewallManager, FMS
from diagrams.aws.security import Guardduty
from diagrams.aws.security import IdentityAndAccessManagementIamAccessAnalyzer, IAMAccessAnalyzer
from diagrams.aws.security import IdentityAndAccessManagementIamAddOn
from diagrams.aws.security import IdentityAndAccessManagementIamAWSStsAlternate
from diagrams.aws.security import IdentityAndAccessManagementIamAWSSts, IAMAWSSts
from diagrams.aws.security import IdentityAndAccessManagementIamDataEncryptionKey
from diagrams.aws.security import IdentityAndAccessManagementIamEncryptedData
from diagrams.aws.security import IdentityAndAccessManagementIamLongTermSecurityCredential
from diagrams.aws.security import IdentityAndAccessManagementIamMfaToken
from diagrams.aws.security import IdentityAndAccessManagementIamPermissions, IAMPermissions
from diagrams.aws.security import IdentityAndAccessManagementIamRole, IAMRole
from diagrams.aws.security import IdentityAndAccessManagementIamTemporarySecurityCredential
from diagrams.aws.security import IdentityAndAccessManagementIam, IAM
from diagrams.aws.security import InspectorAgent
from diagrams.aws.security import Inspector
from diagrams.aws.security import KeyManagementService, KMS
from diagrams.aws.security import Macie
from diagrams.aws.security import ManagedMicrosoftAd
from diagrams.aws.security import ResourceAccessManager, RAM
from diagrams.aws.security import SecretsManager
from diagrams.aws.security import SecurityHubFinding
from diagrams.aws.security import SecurityHub
from diagrams.aws.security import SecurityIdentityAndCompliance
from diagrams.aws.security import ShieldAdvanced
from diagrams.aws.security import Shield
from diagrams.aws.security import SimpleAd
from diagrams.aws.security import SingleSignOn
from diagrams.aws.security import WAFFilteringRule
from diagrams.aws.security import WAF

from diagrams.aws.storage import Backup
from diagrams.aws.storage import CloudendureDisasterRecovery, CDR
from diagrams.aws.storage import EFSInfrequentaccessPrimaryBg
from diagrams.aws.storage import EFSStandardPrimaryBg
from diagrams.aws.storage import ElasticBlockStoreEBSSnapshot
from diagrams.aws.storage import ElasticBlockStoreEBSVolume
from diagrams.aws.storage import ElasticBlockStoreEBS, EBS
from diagrams.aws.storage import ElasticFileSystemEFSFileSystem
from diagrams.aws.storage import ElasticFileSystemEFS, EFS
from diagrams.aws.storage import FsxForLustre
from diagrams.aws.storage import FsxForWindowsFileServer
from diagrams.aws.storage import Fsx, FSx
from diagrams.aws.storage import MultipleVolumesResource
from diagrams.aws.storage import S3GlacierArchive
from diagrams.aws.storage import S3GlacierVault
from diagrams.aws.storage import S3Glacier
from diagrams.aws.storage import SimpleStorageServiceS3BucketWithObjects
from diagrams.aws.storage import SimpleStorageServiceS3Bucket
from diagrams.aws.storage import SimpleStorageServiceS3Object
from diagrams.aws.storage import SimpleStorageServiceS3, S3
from diagrams.aws.storage import SnowFamilySnowballImportExport
from diagrams.aws.storage import SnowballEdge
from diagrams.aws.storage import Snowball
from diagrams.aws.storage import Snowmobile
from diagrams.aws.storage import StorageGatewayCachedVolume
from diagrams.aws.storage import StorageGatewayNonCachedVolume
from diagrams.aws.storage import StorageGatewayVirtualTapeLibrary
from diagrams.aws.storage import StorageGateway
from diagrams.aws.storage import Storage

