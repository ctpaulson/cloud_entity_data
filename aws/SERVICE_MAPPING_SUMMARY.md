# Service Mapping Executive Summary
## First 50 AWS Resource Types - Mapping Analysis

**Date:** 2025-11-21
**Resources Mapped:** 49 of 50
**Resources Skipped:** 1 (non-infrastructure)

---

## Mapping Philosophy Applied

This mapping exercise demonstrates adherence to the colloquial service naming philosophy documented in [CLAUDE.md](../CLAUDE.md). Key principles followed:

### 1. **Judgment Over Pattern Matching**
Rather than automatically mapping resources based on CloudFormation namespace patterns, each resource was evaluated based on:
- AWS marketing and documentation terminology
- Official AWS icon set organization
- Common industry understanding of service boundaries
- User mental models of AWS services

### 2. **Icon Set Validation**
The official AWS icon set (`AWS-Icons_07312025/`) was cross-referenced to validate service existence and categorization. This revealed:
- **391 official services** with AWS-provided icons
- Icon names use hyphenated format (e.g., `AWS-Certificate-Manager`)
- Service definitions use camelCase format (e.g., `CertificateManager`)
- Some CloudFormation namespaces don't correspond to standalone services

### 3. **User Verification for Edge Cases**
Two resources required clarification before mapping:
- **AWS::AccessAnalyzer::Analyzer** - No standalone icon exists; mapped to `IAM`
- **AWS::Alexa::ASK::Skill** - Voice development tool; skipped as non-infrastructure

---

## Mapping Decisions

### Group 1: Certificate Management (4 resources)
**CloudFormation Namespace:** `AWS::ACMPCA::*`
**Mapped To:** `/aws/service/CertificateManager`

**Rationale:**
- ACMPCA = AWS Certificate Manager Private Certificate Authority
- Despite the distinct namespace, this is marketed as part of ACM
- Icon reference: `AWS-Certificate-Manager` in Security-Identity-Compliance category
- Users think of this as "Certificate Manager" not "ACMPCA"

**Resources:**
- AWS::ACMPCA::Certificate
- AWS::ACMPCA::CertificateAuthority
- AWS::ACMPCA::CertificateAuthorityActivation
- AWS::ACMPCA::Permission

### Group 2: Operations Intelligence (1 resource)
**CloudFormation Namespace:** `AWS::AIOps::*`
**Mapped To:** `/aws/service/DevOpsGuru`

**Rationale:**
- AIOps is the CloudFormation namespace for Amazon DevOps Guru
- "AIOps" is not how AWS markets this service
- Icon reference: `AWS-DevOps-Guru` in Management-Governance category
- Demonstrates avoiding pattern-matching on namespace names

**Resources:**
- AWS::AIOps::InvestigationGroup

### Group 3: Security Analysis (1 resource)
**CloudFormation Namespace:** `AWS::AccessAnalyzer::*`
**Mapped To:** `/aws/service/IAM`

**Rationale:**
- IAM Access Analyzer is a feature of IAM, not a standalone service
- **No icon exists** for AccessAnalyzer in the official icon set
- AWS documentation presents this as an IAM capability
- Aligns with AWS's service organization hierarchy

**Resources:**
- AWS::AccessAnalyzer::Analyzer

**Alternative Considered:** Creating a new `AccessAnalyzer` service
**Decision:** Map to IAM based on icon set absence and AWS marketing

### Group 4: Message Broker (3 resources)
**CloudFormation Namespace:** `AWS::AmazonMQ::*`
**Mapped To:** `/aws/service/MQ`

**Rationale:**
- Colloquial name is "Amazon MQ" not "AmazonMQ"
- Icon reference: `Amazon-MQ` in Application-Integration category
- Existing service definition uses shortened name `MQ`
- Demonstrates colloquial naming over technical namespaces

**Resources:**
- AWS::AmazonMQ::Broker
- AWS::AmazonMQ::Configuration
- AWS::AmazonMQ::ConfigurationAssociation

### Group 5: Frontend Development (6 resources)
**CloudFormation Namespace:** `AWS::Amplify::*` and `AWS::AmplifyUIBuilder::*`
**Mapped To:** `/aws/service/Amplify`

**Rationale:**
- Amplify UI Builder is part of the Amplify service family
- Icon reference: `AWS-Amplify` in Front-End-Web-Mobile category
- No separate icon exists for UI Builder
- Users understand this as a unified "Amplify" offering

**Resources:**
- AWS::Amplify::App
- AWS::Amplify::Branch
- AWS::Amplify::Domain
- AWS::AmplifyUIBuilder::Component
- AWS::AmplifyUIBuilder::Form
- AWS::AmplifyUIBuilder::Theme

### Group 6: API Management (34 resources)
**CloudFormation Namespace:** `AWS::ApiGateway::*` and `AWS::ApiGatewayV2::*`
**Mapped To:** `/aws/service/APIGateway`

**Rationale:**
- Both v1 (REST/WebSocket) and v2 (HTTP APIs) are part of API Gateway
- Icon reference: `Amazon-API-Gateway` in Networking-Content-Delivery category
- Version differences are implementation details, not service boundaries
- Users think of "API Gateway" as a single service with multiple API types

**Resources (REST API - 21 resources):**
- AWS::ApiGateway::Account, ApiKey, Authorizer, BasePathMapping, BasePathMappingV2,
- ClientCertificate, Deployment, DocumentationPart, DocumentationVersion, DomainName,
- DomainNameAccessAssociation, DomainNameV2, GatewayResponse, Method, Model,
- RequestValidator, Resource, Stage, UsagePlan, UsagePlanKey, VpcLink

**Resources (HTTP API - 13 resources):**
- AWS::ApiGatewayV2::ApiGatewayManagedOverrides, ApiMapping, Authorizer, Deployment,
- DomainName, Integration, IntegrationResponse, Model, Route, RouteResponse,
- RoutingRule, Stage, VpcLink

### Group 7: Voice Development (1 resource - SKIPPED)
**CloudFormation Namespace:** `AWS::Alexa::ASK::*`
**Decision:** Left unmapped (serviceId remains `null`)

**Rationale:**
- Alexa Skills Kit (ASK) is for voice application development
- Icon reference: `Alexa-For-Business` exists but is a **different product**
- Not a typical cloud infrastructure component
- Users don't visualize voice skills in infrastructure diagrams

**Resources:**
- AWS::Alexa::ASK::Skill (SKIPPED)

---

## Key Takeaways

### 1. **CloudFormation ≠ Service Boundaries**
CloudFormation namespaces often don't match how AWS markets services:
- `ACMPCA` → Part of Certificate Manager
- `AIOps` → DevOps Guru
- `AmazonMQ` → Shortened to MQ
- `AmplifyUIBuilder` → Part of Amplify

### 2. **Icon Set as Ground Truth**
The official icon set proved invaluable for validation:
- **AccessAnalyzer's absence** confirmed it's not a standalone service
- **Alexa-For-Business vs ASK::Skill** revealed they're different products
- Icon categories align with user mental models

### 3. **Infrastructure vs. Development Tools**
Not all CloudFormation resources belong in infrastructure diagrams:
- Alexa Skills Kit is development-focused
- Configuration and code deployment tools may not need visualization
- Focus on resources users want to see in architecture diagrams

### 4. **Version Unity**
Service versions (v1, v2) typically don't create service boundaries:
- API Gateway v1 and v2 are the same service
- Differences are implementation details, not user-facing distinctions

---

## Statistics

- **Total Resources Analyzed:** 50
- **Successfully Mapped:** 49 (98%)
- **Skipped (Non-Infrastructure):** 1 (2%)
- **Services Used:** 6 existing services (IAM, CertificateManager, DevOpsGuru, MQ, Amplify, APIGateway)
- **New Services Created:** 0
- **User Verifications Required:** 2

---

## Recommendations for Future Mapping

1. **Always check the icon set** before creating new services
2. **Consider the user's mental model** - how would they search for this?
3. **Group related resources** even if namespaces differ
4. **Skip development/build tools** that don't appear in infrastructure diagrams
5. **When uncertain, verify** rather than creating unnecessary services

---

## Next Steps

1. ✅ Complete: First 50 resources mapped
2. 🔄 Pending: Map remaining 1,368 unmapped resources
3. 🔄 Pending: Add icon ID field to service definitions
4. 🔄 Pending: Map missing icon-based services to definitions
5. 🔄 Pending: Create validation tooling for consistency checks
