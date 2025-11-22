#!/usr/bin/env python3
"""
Script to bulk map orphaned AWS resources to their services.
"""

import json
import re

def bulk_map_resources(file_path):
    """Bulk map resources from unmapped file to their proper services."""

    # Read the file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Define prefix-based mappings (CFN identifier prefix -> service ID)
    prefix_mappings = {
        # AI/ML
        'AWS::Bedrock::': '/aws/service/Bedrock',
        'AWS::SageMaker::': '/aws/service/SageMakerAI',

        # Security
        'AWS::GuardDuty::': '/aws/service/GuardDuty',
        'AWS::SecurityHub::': '/aws/service/SecurityHub',
        'AWS::WAF::': '/aws/service/WAF',
        'AWS::WAFv2::': '/aws/service/WAF',
        'AWS::WAFRegional::': '/aws/service/WAF',
        'AWS::Macie::': '/aws/service/Macie',
        'AWS::FMS::': '/aws/service/WAF',  # Firewall Manager uses WAF
        'AWS::Shield::': '/aws/service/Shield',

        # Analytics
        'AWS::Glue::': '/aws/service/Glue',
        'AWS::QuickSight::': '/aws/service/QuickSight',
        'AWS::RedshiftServerless::': '/aws/service/Redshift',

        # Governance
        'AWS::ControlTower::': '/aws/service/ControlTower',
        'AWS::SSO::': '/aws/service/IAMIdentityCenter',
        'AWS::IdentityStore::': '/aws/service/IAMIdentityCenter',

        # IoT
        'AWS::IoT::': '/aws/service/IoTCore',
        'AWS::IoTAnalytics::': '/aws/service/IoTAnalytics',
        'AWS::IoTEvents::': '/aws/service/IoTEvents',
        'AWS::IoTFleetHub::': '/aws/service/IoTCore',
        'AWS::IoTFleetWise::': '/aws/service/IoTFleetWise',
        'AWS::IoTSiteWise::': '/aws/service/IoTSiteWise',
        'AWS::IoTThingsGraph::': '/aws/service/IoTCore',
        'AWS::IoTTwinMaker::': '/aws/service/IoTTwinMaker',
        'AWS::IoTWireless::': '/aws/service/IoTCore',
        'AWS::GreengrassV2::': '/aws/service/IoTGreengrass',

        # Networking
        'AWS::GlobalAccelerator::': '/aws/service/GlobalAccelerator',
        'AWS::Route53Resolver::': '/aws/service/Route53',
        'AWS::Route53RecoveryControl::': '/aws/service/Route53',
        'AWS::Route53RecoveryReadiness::': '/aws/service/Route53',
        'AWS::NetworkManager::': '/aws/service/CloudWAN',

        # Storage/Transfer
        'AWS::Transfer::': '/aws/service/TransferFamily',
        'AWS::DataSync::': '/aws/service/DataSync',

        # Additional high-value mappings
        'AWS::CloudFormation::': '/aws/service/CloudFormation',
        'AWS::CloudWatch::': '/aws/service/CloudWatch',
        'AWS::Logs::': '/aws/service/CloudWatch',
        'AWS::Config::': '/aws/service/Config',
        'AWS::KMS::': '/aws/service/KMS',
        'AWS::SecretsManager::': '/aws/service/SecretsManager',
        'AWS::CertificateManager::': '/aws/service/CertificateManager',
        'AWS::ACMPCA::': '/aws/service/CertificateManager',
        'AWS::ECR::': '/aws/service/ECR',
        'AWS::EKS::': '/aws/service/EKS',
        'AWS::Backup::': '/aws/service/Backup',
        'AWS::CodeBuild::': '/aws/service/CodeBuild',
        'AWS::CodeCommit::': '/aws/service/CodeCommit',
        'AWS::CodeDeploy::': '/aws/service/CodeDeploy',
        'AWS::CodePipeline::': '/aws/service/CodePipeline',
        'AWS::Connect::': '/aws/service/Connect',
        'AWS::Detective::': '/aws/service/Detective',
        'AWS::DeviceFarm::': '/aws/service/DeviceFarm',
        'AWS::DirectoryService::': '/aws/service/DirectoryService',
        'AWS::DMS::': '/aws/service/DMS',
        'AWS::ElasticBeanstalk::': '/aws/service/ElasticBeanstalk',
        'AWS::Elasticsearch::': '/aws/service/OpenSearchService',
        'AWS::EventSchemas::': '/aws/service/EventBridge',
        'AWS::FIS::': '/aws/service/FaultInjectionSimulator',
        'AWS::FSx::': '/aws/service/FSx',
        'AWS::GameLift::': '/aws/service/GameLift',
        'AWS::GlobalAccelerator::': '/aws/service/GlobalAccelerator',
        'AWS::Grafana::': '/aws/service/ManagedGrafana',
        'AWS::GroundStation::': '/aws/service/GroundStation',
        'AWS::HealthLake::': '/aws/service/HealthLake',
        'AWS::IAM::': '/aws/service/IAM',
        'AWS::Inspector::': '/aws/service/Inspector',
        'AWS::InspectorV2::': '/aws/service/Inspector',
        'AWS::IVS::': '/aws/service/IVS',
        'AWS::Kendra::': '/aws/service/Kendra',
        'AWS::KinesisAnalytics::': '/aws/service/KinesisDataAnalytics',
        'AWS::KinesisAnalyticsV2::': '/aws/service/KinesisDataAnalytics',
        'AWS::KinesisVideo::': '/aws/service/KinesisVideoStreams',
        'AWS::LakeFormation::': '/aws/service/LakeFormation',
        'AWS::Lex::': '/aws/service/Lex',
        'AWS::Location::': '/aws/service/LocationService',
        'AWS::Lookout::': '/aws/service/LookoutForEquipment',
        'AWS::MediaConnect::': '/aws/service/MediaConnect',
        'AWS::MediaConvert::': '/aws/service/MediaConvert',
        'AWS::MediaLive::': '/aws/service/MediaLive',
        'AWS::MediaPackage::': '/aws/service/MediaPackage',
        'AWS::MediaStore::': '/aws/service/MediaStore',
        'AWS::MediaTailor::': '/aws/service/MediaTailor',
        'AWS::MemoryDB::': '/aws/service/MemoryDB',
        'AWS::Neptune::': '/aws/service/Neptune',
        'AWS::NetworkFirewall::': '/aws/service/NetworkFirewall',
        'AWS::OpenSearchServerless::': '/aws/service/OpenSearchServerless',
        'AWS::OpenSearchService::': '/aws/service/OpenSearchService',
        'AWS::Organizations::': '/aws/service/Organizations',
        'AWS::OSIS::': '/aws/service/OpenSearchService',
        'AWS::Pinpoint::': '/aws/service/Pinpoint',
        'AWS::Pipes::': '/aws/service/EventBridge',
        'AWS::QLDB::': '/aws/service/QLDB',
        'AWS::RAM::': '/aws/service/ResourceAccessManager',
        'AWS::Rekognition::': '/aws/service/Rekognition',
        'AWS::ResilienceHub::': '/aws/service/ResilienceHub',
        'AWS::ResourceExplorer2::': '/aws/service/ResourceExplorer',
        'AWS::ResourceGroups::': '/aws/service/ResourceGroups',
        'AWS::Route53::': '/aws/service/Route53',
        'AWS::S3::': '/aws/service/S3',
        'AWS::S3ObjectLambda::': '/aws/service/S3',
        'AWS::S3Outposts::': '/aws/service/S3',
        'AWS::Scheduler::': '/aws/service/EventBridge',
        'AWS::ServiceCatalog::': '/aws/service/ServiceCatalog',
        'AWS::ServiceDiscovery::': '/aws/service/CloudMap',
        'AWS::SES::': '/aws/service/SES',
        'AWS::SNS::': '/aws/service/SNS',
        'AWS::SQS::': '/aws/service/SQS',
        'AWS::SSM::': '/aws/service/SystemsManager',
        'AWS::Synthetics::': '/aws/service/CloudWatch',
        'AWS::Timestream::': '/aws/service/Timestream',
        'AWS::VoiceID::': '/aws/service/Connect',
        'AWS::VPCLattice::': '/aws/service/VPCLattice',
        'AWS::Wisdom::': '/aws/service/Connect',
        'AWS::WorkSpaces::': '/aws/service/WorkSpaces',
        'AWS::XRay::': '/aws/service/XRay',
    }

    # Update resource types
    changes_made = 0
    for resource in data.get('ResourceTypes', []):
        cfn_id = resource.get('cfnIdentifier')
        current_service = resource.get('serviceId')

        # Skip if already mapped to a service (not null and not generic EC2)
        if current_service and current_service != '/aws/service/EC2':
            continue

        # Try to find a matching prefix
        for prefix, new_service in prefix_mappings.items():
            if cfn_id and cfn_id.startswith(prefix):
                resource['serviceId'] = new_service
                changes_made += 1
                print(f"Mapped {cfn_id}: {current_service} -> {new_service}")
                break

    # Write back to file
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"\nTotal resources bulk mapped: {changes_made}")
    return changes_made

if __name__ == '__main__':
    file_path = '/home/user/cloud_entity_data/aws/resourcetype-unmapped.json'
    bulk_map_resources(file_path)
