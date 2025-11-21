# AWS Resources by Category

This document organizes AWS mapped resources by category and service.

# Analytics

## Amazon EMR

- **EMRCluster** (AWS::EMR::Cluster)

## Amazon Data Firehose

- **KinesisFirehoseDeliveryStream** (AWS::KinesisFirehose::DeliveryStream)

## Amazon Kinesis Data Streams

- **KinesisStream** (AWS::Kinesis::Stream)

## Amazon OpenSearch Service

- **ElasticsearchDomain** (AWS::Elasticsearch::Domain)

## Amazon Redshift

- **RedshiftCluster** (AWS::Redshift::Cluster)

## Amazon Managed Streaming for Apache Kafka (Amazon MSK)

- **MSKCluster** (AWS::MSK::Cluster)

# Application integration

## AWS Step Functions

- **StepFunctionsActivity** (AWS::StepFunctions::Activity)
- **StepFunctionsStateMachine** (AWS::StepFunctions::StateMachine)

## Amazon EventBridge

- **EventBridgeEventBus** (AWS::Events::EventBus)
- **EventBridgeRule** (AWS::Events::Rule)

## Amazon Simple Notification Service

- **SNSSubscription** (AWS::SNS::Subscription)
- **SNSTopic** (AWS::SNS::Topic)

## Amazon Simple Queue Service

- **SQSQueue** (AWS::SQS::Queue)

# Compute

## Amazon EC2

- **EC2CustomerGateway** (AWS::EC2::CustomerGateway)
- **EC2Instance** (AWS::EC2::Instance)
- **EC2NetworkInterface** (AWS::EC2::NetworkInterface)
- **EC2InternetGateway** (AWS::EC2::InternetGateway)
- **EC2NATGateway** (AWS::EC2::NatGateway)
- **EC2NetworkAcl** (AWS::EC2::NetworkAcl)
- **EC2RouteTable** (AWS::EC2::RouteTable)
- **EC2SecurityGroup** (AWS::EC2::SecurityGroup)
- **EC2Subnet** (AWS::EC2::Subnet)
- **EC2TransitGateway** (AWS::EC2::TransitGateway)
- **EC2Volume** (AWS::EC2::Volume)
- **EC2VPC** (AWS::EC2::VPC)
- **EC2VPCEndpoint** (AWS::EC2::VPCEndpoint)
- **EC2VPCEndpointConnectionNotification** (AWS::EC2::VPCEndpointConnectionNotification)
- **EC2VPCPeeringConnection** (AWS::EC2::VPCPeeringConnection)
- **EC2VPNConnection** (AWS::EC2::VPNConnection)
- **EC2VPNGateway** (AWS::EC2::VPNGateway)

## Amazon EC2 Auto Scaling

- **AutoScalingGroup** (AWS::AutoScaling::AutoScalingGroup)
- **AutoScalingLaunchConfiguration** (AWS::AutoScaling::LaunchConfiguration)

## AWS Lambda

- **LambdaEventSourceMapping** (AWS::Lambda::EventSourceMapping)
- **LambdaFunction** (AWS::Lambda::Function)

# Containers

## Amazon Elastic Container Registry

- **ECRRegistryPolicy** (AWS::ECR::RegistryPolicy)

## Amazon Elastic Container Service

- **ECSCluster** (AWS::ECS::Cluster)
- **ECSService** (AWS::ECS::Service)
- **ECSTaskDefinition** (AWS::ECS::TaskDefinition)

## Amazon Elastic Kubernetes Service

- **EKSCluster** (AWS::EKS::Cluster)

# Databases

## Amazon DynamoDB

- **DynamoDBTable** (AWS::DynamoDB::Table)

## Amazon ElastiCache

- **ElastiCacheCacheCluster** (AWS::ElastiCache::CacheCluster)

## Amazon Relational Database Service

- **RDSDBInstance** (AWS::RDS::DBInstance)
- **RDSDBCluster** (AWS::RDS::DBCluster)
- **RDSDBProxy** (AWS::RDS::DBProxy)

## Amazon DocumentDB (with MongoDB compatibility)

- **DocumentDBCluster** (AWS::DocDB::DBCluster)

# Frontend web and mobile services

## AWS AppSync

- **AppSyncGraphQLApi** (AWS::AppSync::GraphQLApi)

# Management and governance

## AWS CloudTrail

- **CloudTrailTrail** (AWS::CloudTrail::Trail)

# Networking and content delivery

## Amazon API Gateway

- **APIGatewayRestApi** (AWS::ApiGateway::RestApi)
- **APIGatewayV2Api** (AWS::ApiGatewayV2::Api)

## Amazon CloudFront

- **CloudFrontDistribution** (AWS::CloudFront::Distribution)

## Elastic Load Balancing

- **ELBLoadBalancer** (AWS::ElasticLoadBalancing::LoadBalancer)
- **ELBV2LoadBalancer** (AWS::ElasticLoadBalancingV2::LoadBalancer)
- **ELBV2TargetGroup** (AWS::ElasticLoadBalancingV2::TargetGroup)

## Amazon Route 53

- **Route53HostedZone** (AWS::Route53::HostedZone)

# Security, identity, and compliance

## Amazon Cognito

- **CognitoUserPool** (AWS::Cognito::UserPool)

## AWS Identity and Access Management

- **IAMRole** (AWS::IAM::Role)

## AWS Network Firewall

- **NetworkFirewall** (AWS::NetworkFirewall::Firewall)

# Storage

## Amazon Elastic File System

- **EFSFileSystem** (AWS::EFS::FileSystem)

## Amazon Simple Storage Service

- **S3Bucket** (AWS::S3::Bucket)
