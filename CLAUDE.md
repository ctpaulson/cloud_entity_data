# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository maintains structured metadata about cloud resources across AWS, Azure, and Google Cloud Platform (GCP). It provides a hierarchical taxonomy of cloud services organized by categories and includes resource type mappings for infrastructure-as-code tools.

## Project Structure

The repository is organized into three cloud provider directories:

```
aws/
├── category.json                              # Category definitions
├── resourcetype-mapped.json                   # CloudFormation resource type mappings
├── canonical-resource-types-Angel-spike.csv   # Full CFN identifier reference
└── service/                                   # Service definitions by category
    ├── Analytics.json
    ├── Compute.json
    └── [other categories...]

azure/
├── category.json                              # Category definitions
├── resourcetype-mapped.json                   # Azure resource type mappings
└── service/                                   # Service definitions by category
    ├── Analytics.json
    ├── Compute.json
    └── [other categories...]

gcp/
├── category.json                              # Category definitions
├── resourcetype-mapped.json                   # GCP resource type mappings
└── service/                                   # Service definitions by category
    ├── Analytics.json
    ├── Compute.json
    └── [other categories...]

aws_resources_by_category.md                   # Human-readable AWS resource reference
```

## Data Model

### Categories (`category.json`)

Categories group related cloud services by functional domain. Each category has:
- `id`: Unique identifier (format: `/[provider]/category/[name]`)
- `fullName`: Complete display name
- `shortName`: Abbreviated name
- `description`: Purpose and scope of the category

**Common categories across providers:**
- Analytics
- Compute
- Containers
- Databases
- Security
- Networking
- Storage
- AI/ML
- Developer Tools
- Management

### Services (`service/*.json`)

Each category file contains an array of services. Service objects include:
- `id`: Unique identifier (format: `/[provider]/service/[name]`)
- `fullName`: Official service name
- `shortName`: Abbreviated service name
- `description`: Detailed service capabilities and use cases
- `categoryId`: Reference to parent category
- `isCore`: (GCP only) Boolean indicating core vs. specialized services

### Resource Types (`resourcetype-mapped.json` - AWS only)

AWS resource types map CloudFormation identifiers to internal type systems:
- `id`: Internal identifier (format: `aws/resourcetype/[name]`)
- `cfnIdentifier`: CloudFormation resource type (format: `AWS::[Service]::[Resource]`)
- `typeIdentifier`: Internal type enumeration (format: `AwsResourceTypes.[Type]`)
- `serviceId`: Reference to parent service
- `isMapped`: Boolean indicating mapping status

## Working with the Data

### Adding a New Service

1. Identify the appropriate category for the service
2. Open the corresponding `service/[Category].json` file
3. Add a new service object to the array:
   ```json
   {
     "id": "/[provider]/service/[ServiceName]",
     "fullName": "Full Service Name",
     "shortName": "Short Name",
     "description": "Detailed description...",
     "categoryId": "/[provider]/category/[CategoryName]"
   }
   ```
4. For GCP services, include `isCore: true/false`

### Adding a New Category

1. Open `category.json` in the appropriate provider directory
2. Add category definition to the Categories array
3. Create a new `service/[CategoryName].json` file
4. Add relevant services to the new category file

### Adding AWS Resource Type Mappings

1. Open `aws/resourcetype-mapped.json`
2. Add resource type definition to ResourceTypes array:
   ```json
   {
     "id": "aws/resourcetype/[ResourceName]",
     "cfnIdentifier": "AWS::[Service]::[Resource]",
     "typeIdentifier": "AwsResourceTypes.[Type]",
     "serviceId": "/aws/service/[ServiceId]",
     "isMapped": true
   }
   ```
3. Update `aws_resources_by_category.md` to include human-readable documentation

### Validating Data Consistency

When modifying files, ensure:
- All `serviceId` references point to existing services
- All `categoryId` references point to existing categories
- ID formats follow the established patterns
- JSON is properly formatted and valid
- CloudFormation identifiers match official AWS documentation

## File Relationships

The data structure maintains referential integrity:

1. **Service → Category**: Each service file references its parent category via `categoryId`
2. **Resource Type → Service** (AWS): Each resource type references its service via `serviceId`
3. **Service Category → Service File**: Services are physically organized in files matching their category name

When modifying services, you may need to update multiple files to maintain consistency.

## Best Practices

- **Preserve official terminology**: Use exact service names and descriptions from provider documentation
- **Maintain ID conventions**: Follow the established ID patterns (`/provider/type/name`)
- **Keep descriptions current**: Service descriptions should reflect current capabilities
- **Cross-reference updates**: When updating service definitions, check if resource type mappings need updates
- **Validate JSON**: Ensure all JSON files are syntactically valid before committing
