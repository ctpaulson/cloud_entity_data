# AWS Entity Data Updates - Summary

## Changes Made on 2025-11-22

This update implements the recommendations from the AWS Entity Data Analysis & Cleanup Report.

### Part 1: Resource Type Mapping Corrections (27 resources updated)

#### Network Resource Granularity
Moved EC2 networking resources to their specific services:

**Client VPN** (4 resources) → `/aws/service/VPN`:
- AWS::EC2::ClientVpnAuthorizationRule
- AWS::EC2::ClientVpnEndpoint
- AWS::EC2::ClientVpnRoute
- AWS::EC2::ClientVpnTargetNetworkAssociation

**Verified Access** (4 resources) → `/aws/service/VerifiedAccess`:
- AWS::EC2::VerifiedAccessEndpoint
- AWS::EC2::VerifiedAccessGroup
- AWS::EC2::VerifiedAccessInstance
- AWS::EC2::VerifiedAccessTrustProvider

**VPC Features** (18 resources) → `/aws/service/VPC`:
- IPAM resources (7): IPAM, IPAMAllocation, IPAMPool, IPAMPoolCidr, IPAMResourceDiscovery, IPAMResourceDiscoveryAssociation, IPAMScope
- Network Insights (4): NetworkInsightsAccessScope, NetworkInsightsAccessScopeAnalysis, NetworkInsightsAnalysis, NetworkInsightsPath
- Traffic Mirroring (4): TrafficMirrorFilter, TrafficMirrorFilterRule, TrafficMirrorSession, TrafficMirrorTarget
- Other VPC (3): FlowLog, PrefixList, Route

**Compute Granularity** (1 resource) → `/aws/service/NitroEnclaves`:
- AWS::EC2::EnclaveCertificateIamRoleAssociation

### Part 2: New Service Definitions

Created 2 new service definitions:

1. **AWS RoboMaker** (`/aws/service/RoboMaker`)
   - Added to ML.json
   - Correctly separates RoboMaker from DeepRacer
   - 6 resources remapped from DeepRacer

2. **Amazon SimpleDB** (`/aws/service/SimpleDB`)
   - Added to Databases.json
   - Legacy service distinction from DynamoDB
   - 1 resource remapped from DynamoDB

### Part 3: Service Logic Error Fixes (11 resources updated)

**RoboMaker Resources** (6) → `/aws/service/RoboMaker`:
- AWS::RoboMaker::Fleet
- AWS::RoboMaker::Robot
- AWS::RoboMaker::RobotApplication
- AWS::RoboMaker::RobotApplicationVersion
- AWS::RoboMaker::SimulationApplication
- AWS::RoboMaker::SimulationApplicationVersion

**SimpleDB Resources** (1) → `/aws/service/SimpleDB`:
- AWS::SDB::Domain

**AppIntegrations Resources** (3) → `/aws/service/Connect`:
- AWS::AppIntegrations::Application
- AWS::AppIntegrations::DataIntegration
- AWS::AppIntegrations::EventIntegration

**Alexa Resources** (1) → `null` (explicitly unmapped):
- AWS::Alexa::ASK::Skill (development tool, not infrastructure)

### Part 4: Service Icon Path Updates (4 services)

Added missing icon paths to existing services:

1. **VMware Cloud on AWS**: `AWS-Icons_07312025/Compute/Amazon-Elastic-VMware-Service/Service_Amazon-Elastic-VMware-Service.svg`
2. **AWS Snow Family**: `AWS-Icons_07312025/Storage/AWS-Snowball/Service_AWS-Snowball.svg`
3. **Amazon WorkSpaces Web**: `AWS-Icons_07312025/End-User-Computing/Amazon-WorkSpaces-Family/Service_Amazon-WorkSpaces-Family.svg`
4. **Amazon OpenSearch Serverless**: `AWS-Icons_07312025/Analytics/Amazon-OpenSearch-Service/Service_Amazon-OpenSearch-Service.svg`

## Summary Statistics

- **Total resource type mappings updated**: 38
- **New services created**: 2
- **Service icon paths added**: 4
- **Files modified**: 7

## Impact

These changes improve the accuracy and consistency of AWS resource type mappings by:
1. Using colloquial service names that match AWS marketing and user expectations
2. Properly distinguishing between distinct AWS products
3. Improving icon coverage from 93.2% to 94.9% (220/234 services)
4. Ensuring resources are mapped to their most specific, appropriate service
