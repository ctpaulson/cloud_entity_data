#!/usr/bin/env python3
"""
Script to fix service logic errors in resource type mappings.
"""

import json

def update_service_logic(file_path):
    """Update resource type mappings for service logic fixes."""

    # Read the file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Define mapping updates
    updates = {
        # RoboMaker resources
        'AWS::RoboMaker::Fleet': '/aws/service/RoboMaker',
        'AWS::RoboMaker::Robot': '/aws/service/RoboMaker',
        'AWS::RoboMaker::RobotApplication': '/aws/service/RoboMaker',
        'AWS::RoboMaker::RobotApplicationVersion': '/aws/service/RoboMaker',
        'AWS::RoboMaker::SimulationApplication': '/aws/service/RoboMaker',
        'AWS::RoboMaker::SimulationApplicationVersion': '/aws/service/RoboMaker',

        # SimpleDB resources
        'AWS::SDB::Domain': '/aws/service/SimpleDB',

        # AppIntegrations resources (should map to Connect, not EventBridge)
        'AWS::AppIntegrations::Application': '/aws/service/Connect',
        'AWS::AppIntegrations::DataIntegration': '/aws/service/Connect',
        'AWS::AppIntegrations::EventIntegration': '/aws/service/Connect',
    }

    # Special handling for Alexa::ASK::Skill - set to null (unmapped)
    alexa_skill_cfn = 'AWS::Alexa::ASK::Skill'

    # Update resource types
    changes_made = 0
    for resource in data.get('ResourceTypes', []):
        cfn_id = resource.get('cfnIdentifier')

        # Handle Alexa Skill - set to null
        if cfn_id == alexa_skill_cfn:
            old_service = resource.get('serviceId')
            if old_service is not None:
                resource['serviceId'] = None
                changes_made += 1
                print(f"Updated {cfn_id}: {old_service} -> null (unmapped)")

        # Handle other updates
        elif cfn_id in updates:
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
    update_service_logic(file_path)
