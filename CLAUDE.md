# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository maintains structured metadata about cloud resources across AWS, Azure, and Google Cloud Platform (GCP). It provides a hierarchical taxonomy of cloud services organized by categories and includes resource type mappings for infrastructure-as-code tools.

## Project Structure

The repository is organized into three cloud provider directories:

```
aws/
├── category.json                              # Category definitions
├── resourcetype-mapped.json                   # CloudFormation resource type mappings (59 mapped)
├── resourcetype-unmapped.json                 # Unmapped resource types (1,418 unmapped)
├── canonical-resource-types-Angel-spike.csv   # Full CFN identifier reference (1,477 total)
├── canonical-resource-types-unmapped.csv      # Filtered unmapped resources only
├── AWS-Icons_07312025/                        # Official AWS service icons by category (391 services)
│   ├── Analytics/
│   ├── Compute/
│   ├── Security-Identity-Compliance/
│   └── [24 more categories...]
└── service/                                   # Service definitions by category (234 services)
    ├── Analytics.json
    ├── Compute.json
    └── [21 more categories...]

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
- `isMapped`: Boolean indicating mapped vs. unmapped status

**Mapped vs. Unmapped Resource Types**
Resource types may be either "mapped" or "unmapped". This is a designation of the level of support each resource type has within our product, NOT the level of mapping of metadata in this repository.

*Mapped resource: A cloud resource that we can automatically place in a meaningful, hierarchically correct location on the canvas.*
- A resource is considered "mapped" when Lucid has high confidence in its precise location within a user's cloud environment's structure (e.g., inside a specific VPC and Subnet, rather than just at the Account level).
- Lucid's ability to place a mapped resource correctly can depend on the structure settings configured for the current view.
- Even if a more precise location could theoretically exist, a resource is still considered mapped as long as Lucid can place it in a location that is more specific than the top-level environment (Account, Subscription, or Project).

*Unmapped resource: A cloud resource that was discovered during the import process but cannot be automatically placed on the canvas by Lucid.*
- Unmapped resources appear in the resource explorer but must be placed on the canvas by a user.
- A resource may be unmapped for several reasons:
  - Insufficient Metadata: The cloud provider's APIs may not provide the necessary data to determine its location.
  - Lack of Lucid Support: Lucid has not yet developed automatic placement support for this specific resource type.
  - Configuration-Only Resource: The resource is primarily a configuration setting for another resource and doesn't have its own logical place in a diagram.
  - Incomplete Import: The necessary metadata was not imported due to credential permissions, user settings during the import, or an error during the import process.
- Manual placement: Users can place an unmapped resource by dragging it from the Resources Panel and placing it inside a container shape (like a Subnet). Once they do this, Lucid "trusts" their placement and treats the resource as a managed shape in that location across all relevant views in the document.

**Important: Service Mapping Philosophy**

This repository uses **colloquial service names** that reflect common usage and marketing terminology, rather than strict SDK/API technical names. This approach provides better organization and matches how users think about AWS services.

**Key Examples:**
- **Amazon VPC** is its own service (`/aws/service/VPC`), even though CloudFormation types are `AWS::EC2::VPC*` and the SDK groups it under EC2
- **Amazon EBS** is separate (`/aws/service/EBS`) despite `AWS::EC2::Volume` in CloudFormation
- **AWS Transit Gateway** is distinct (`/aws/service/TransitGateway`) though technically part of EC2

**Mapping Guidelines:**
- Use **judgment based on training data** and common AWS terminology, not pattern matching on CloudFormation identifiers
- Consider how AWS markets and documents the service
- **Cross-reference with AWS icon set** (`AWS-Icons_07312025/`) - the official icons represent AWS's marketing perspective on services
- If a resource belongs to a service not yet in the repository, **VERIFY WITH THE USER** before creating a new service definition
- Do not automatically create services based on CloudFormation namespace patterns (e.g., `AWS::NewService::*` doesn't automatically mean create `/aws/service/NewService`)

**Icon Directory Reference:**
- AWS provides official service icons in `aws/AWS-Icons_07312025/` organized by 27 categories
- Icon names use hyphenated format (e.g., `AWS-Amplify`, `Amazon-EC2`)
- Service definitions use camelCase format (e.g., `Amplify`, `EC2`)
- The icon set contains 391 services - some services in definitions may not have icons, and some icons may not have service definitions yet
- When in doubt about a service's existence or categorization, check if it has an official AWS icon

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

1. Open `aws/resourcetype-mapped.json` or `aws/resourcetype-unmapped.json`
2. **Determine the correct service mapping:**
   - Review existing services in `aws/service/` directory
   - Use colloquial service names, NOT CloudFormation namespace patterns
   - Example: `AWS::EC2::VPC` maps to `/aws/service/VPC`, not `/aws/service/EC2`
   - **If the service doesn't exist, STOP and verify with the user before proceeding**
3. Add resource type definition to ResourceTypes array:
   ```json
   {
     "id": "aws/resourcetype/[ResourceName]",
     "cfnIdentifier": "AWS::[Service]::[Resource]",
     "typeIdentifier": "AwsResourceTypes.[Type]",
     "serviceId": "/aws/service/[ServiceId]",
     "isMapped": true
   }
   ```
4. Update `aws_resources_by_category.md` to include human-readable documentation

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
- **Service mapping discipline**: Always map resources to colloquial service names, never create new services without user verification
- **Resist pattern matching**: Don't assume CloudFormation namespaces (e.g., `AWS::ServiceX::*`) correspond to service definitions
