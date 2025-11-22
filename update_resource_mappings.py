#!/usr/bin/env python3
"""
Script to update AWS resource type mappings according to the analysis report.
"""

import json
import sys

def update_resource_mappings(file_path):
    """Update resource type mappings in the unmapped JSON file."""

    # Read the file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Define mapping updates: old_service -> new_service for specific cfnIdentifier patterns
    updates = {
        # Network Resource Granularity - ClientVPN
        'AWS::EC2::ClientVpnAuthorizationRule': '/aws/service/VPN',
        'AWS::EC2::ClientVpnEndpoint': '/aws/service/VPN',
        'AWS::EC2::ClientVpnRoute': '/aws/service/VPN',
        'AWS::EC2::ClientVpnTargetNetworkAssociation': '/aws/service/VPN',

        # Network Resource Granularity - Verified Access
        'AWS::EC2::VerifiedAccessEndpoint': '/aws/service/VerifiedAccess',
        'AWS::EC2::VerifiedAccessGroup': '/aws/service/VerifiedAccess',
        'AWS::EC2::VerifiedAccessInstance': '/aws/service/VerifiedAccess',
        'AWS::EC2::VerifiedAccessTrustProvider': '/aws/service/VerifiedAccess',

        # Network Resource Granularity - IPAM (VPC feature)
        'AWS::EC2::IPAM': '/aws/service/VPC',
        'AWS::EC2::IPAMAllocation': '/aws/service/VPC',
        'AWS::EC2::IPAMPool': '/aws/service/VPC',
        'AWS::EC2::IPAMPoolCidr': '/aws/service/VPC',
        'AWS::EC2::IPAMResourceDiscovery': '/aws/service/VPC',
        'AWS::EC2::IPAMResourceDiscoveryAssociation': '/aws/service/VPC',
        'AWS::EC2::IPAMScope': '/aws/service/VPC',

        # Network Resource Granularity - VPC features
        'AWS::EC2::FlowLog': '/aws/service/VPC',
        'AWS::EC2::PrefixList': '/aws/service/VPC',
        'AWS::EC2::TrafficMirrorFilter': '/aws/service/VPC',
        'AWS::EC2::TrafficMirrorFilterRule': '/aws/service/VPC',
        'AWS::EC2::TrafficMirrorSession': '/aws/service/VPC',
        'AWS::EC2::TrafficMirrorTarget': '/aws/service/VPC',
        'AWS::EC2::NetworkInsightsAccessScope': '/aws/service/VPC',
        'AWS::EC2::NetworkInsightsAccessScopeAnalysis': '/aws/service/VPC',
        'AWS::EC2::NetworkInsightsAnalysis': '/aws/service/VPC',
        'AWS::EC2::NetworkInsightsPath': '/aws/service/VPC',
        'AWS::EC2::Route': '/aws/service/VPC',

        # Compute Granularity - Nitro Enclaves
        'AWS::EC2::EnclaveCertificateIamRoleAssociation': '/aws/service/NitroEnclaves',
    }

    # Update resource types
    changes_made = 0
    for resource in data.get('ResourceTypes', []):
        cfn_id = resource.get('cfnIdentifier')
        if cfn_id in updates:
            old_service = resource.get('serviceId')
            new_service = updates[cfn_id]
            if old_service != new_service:
                resource['serviceId'] = new_service
                changes_made += 1
                print(f"Updated {cfn_id}: {old_service} -> {new_service}")

    # Write back to file
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"\nTotal changes made: {changes_made}")
    return changes_made

if __name__ == '__main__':
    file_path = '/home/user/cloud_entity_data/aws/resourcetype-unmapped.json'
    update_resource_mappings(file_path)
