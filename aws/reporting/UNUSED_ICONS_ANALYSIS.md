# Unused Icons Analysis & Recommendations

**Date:** 2025-11-21
**Total Unused Icons:** 101
**Already Handled:** 6 (manually matched)
**Remaining for Review:** 95

---

## Already Handled (6 icons)

These icons were manually matched to existing services and should be removed from the "unused" list:

1. ✅ `Amazon-Simple-Email-Service` → `/aws/service/SES`
2. ✅ `Amazon-Augmented-AI-A2I` → `/aws/service/AugmentedAI`
3. ✅ `AWS-Health-Dashboard` → `/aws/service/Health`
4. ✅ `AWS-Elemental-Appliances-&-Software` → `/aws/service/ElementalAppliancesAndSoftware`
5. ✅ `Amazon-VPC` → `/aws/service/VPC`
6. ✅ `Amazon-EFS` → `/aws/service/EFS`

---

## Category 1: Clear Additions - Standalone Services (28 icons)

These are legitimate standalone services that should be added:

### Analytics (3)
1. **AWS Glue DataBrew** - Visual data preparation tool
2. **Amazon Kinesis** - Real-time data streaming (parent service)
3. **Amazon SageMaker** - Full ML platform (parent service vs SageMaker AI)

### AI/ML (5)
4. **Amazon Nova** - New foundation model family
5. **AWS HealthImaging** - Medical imaging service
6. **AWS HealthOmics** - Genomics/omics data service
7. **AWS Neuron** - ML inference chip SDK
8. **Amazon Elastic Inference** - GPU acceleration for inference

### Blockchain (1)
9. **Amazon Quantum Ledger Database (QLDB)** - Ledger database

### Business Applications (3)
10. **AWS Supply Chain** - Supply chain management
11. **AWS End User Messaging** - Messaging service (may replace/complement Pinpoint)
12. **AWS Wickr** - Secure communications

### Compute (9)
13. **AWS Local Zones** - Edge compute locations
14. **AWS Nitro Enclaves** - Isolated compute environments
15. **AWS Outposts family** - On-premises AWS
16. **AWS Outposts servers** - Server variant of Outposts
17. **AWS Parallel Computing Service** - HPC service
18. **AWS SimSpace Weaver** - Spatial simulation service
19. **Bottlerocket** - Container-optimized OS
20. **Elastic Fabric Adapter** - HPC networking
21. **NICE EnginFrame** - HPC portal

### Management (5)
22. **AWS Chatbot** - Slack/Teams integration for AWS
23. **AWS Resilience Hub** - Resilience assessment
24. **AWS Resource Explorer** - Cross-region resource search
25. **AWS Telco Network Builder** - Telecom network automation
26. **AWS Management Console** - Web console (may skip)

### Networking (2)
27. **AWS Cloud WAN** - Global WAN management
28. **Amazon Application Recovery Controller** - Multi-region recovery

---

## Category 2: Granularity Questions - Need User Decision (20 icons)

### A. SageMaker Sub-Services (2)
**Question:** Should these be separate services or features of SageMaker AI?
- `Amazon-SageMaker-Ground-Truth` - Data labeling
- `Amazon-SageMaker-Studio-Lab` - Free ML development

**Recommendation:** Keep as features of SageMaker AI (don't add separate services)

### B. ML Framework Variants (3)
**Question:** Should ML frameworks be services or skip?
- `Apache-MXNet-on-AWS`
- `PyTorch-on-AWS`
- `TensorFlow-on-AWS`

**Recommendation:** Skip - these are frameworks, not services

### C. AWS Deep Learning Tools (2)
**Question:** Infrastructure tools or services?
- `AWS-Deep-Learning-AMIs` - Pre-configured AMIs
- `AWS-Deep-Learning-Containers` - Pre-configured containers

**Recommendation:** Skip - these are infrastructure artifacts

### D. Container Deployment Variants (4)
**Question:** Are these separate services or deployment options?
- `Amazon-ECS-Anywhere` - ECS on-premises
- `Amazon-EKS-Anywhere` - EKS on-premises
- `Amazon-EKS-Cloud` - Cloud variant designation
- `Amazon-EKS-Distro` - Kubernetes distribution

**Recommendation:** Skip EKS-Cloud/Distro (not services), consider adding ECS/EKS Anywhere as service variants

### E. VPN Service Split (2)
**Question:** Should VPN be split or remain unified?
- `AWS-Client-VPN` - Remote access VPN
- `AWS-Site-to-Site-VPN` - Network-to-network VPN (currently used)

**Recommendation:** Keep unified VPN service (current state is correct)

### F. Outposts Variants (2)
**Question:** Family vs servers - separate or unified?
- `AWS-Outposts-family` - Product line
- `AWS-Outposts-servers` - Server variant

**Recommendation:** Add "Outposts family" as the main service, skip servers variant

### G. AWS Thinkbox Suite (6 icons)
**Question:** Individual services or product suite?
- `AWS-Thinkbox-Deadline` - Render management
- `AWS-Thinkbox-Frost` - Particle effects
- `AWS-Thinkbox-Krakatoa` - Volumetric rendering
- `AWS-Thinkbox-Sequoia` - Geometry
- `AWS-Thinkbox-Stoke` - Particle simulation
- `AWS-Thinkbox-XMesh` - Geometry caching

**Recommendation:** Add "AWS Thinkbox" as umbrella service, not individual tools

### H. Elemental Sub-Products (4 + 1 already handled)
**Question:** Individual services or part of Elemental Appliances?
- `AWS-Elemental-Conductor` - Workflow orchestration
- `AWS-Elemental-Delta` - Live encoding
- `AWS-Elemental-Link` - Hardware encoder
- `AWS-Elemental-Live` - Live encoding software
- `AWS-Elemental-Server` - VOD encoding
- ✅ `AWS-Elemental-Appliances-&-Software` (already added as umbrella)

**Recommendation:** Keep umbrella service "Elemental Appliances and Software" (current state)

---

## Category 3: Infrastructure/Tooling - Skip (12 icons)

These are development tools, SDKs, or infrastructure components, not cloud services:

1. **AWS Cloud Development Kit** - Infrastructure as code framework
2. **AWS Command Line Interface** - CLI tool
3. **AWS Tools and SDKs** - Developer tools
4. **AWS Cloud Control API** - API layer
5. **AWS Application Auto Scaling** - Feature, not service
6. **AWS AppConfig** - Feature of Systems Manager
7. **AWS Backint Agent** - SAP backup agent
8. **AWS Distro for OpenTelemetry** - Observability distribution
9. **AWS Parallel Cluster** - HPC cluster management tool
10. **Amazon DCV** - Remote desktop protocol
11. **AWS App Studio** - Low-code development (very new)
12. **Amazon CodeWhisperer** - Now part of Amazon Q

---

## Category 4: Customer Enablement - Skip (6 icons)

Not technical cloud services:

1. **AWS Activate** - Startup program
2. **AWS IQ** - Expert marketplace
3. **AWS Professional Services** - Consulting
4. **AWS Support** - Support plans
5. **AWS Training & Certification** - Educational programs
6. **AWS rePost Private** - Community forum

---

## Category 5: Service Variants/Sub-Components (15 icons)

These are variants or components of existing services:

### Database
1. **Oracle Database at AWS** - Database variant (RDS supports Oracle)

### Gaming
2. **Amazon GameLift Streams** - Feature of GameLift
3. **Open 3D Engine** - Game engine (not a service)

### Business
4. **Alexa For Business** - Separate from Alexa Skills Kit
5. **Amazon Pinpoint APIs** - API layer for Pinpoint
6. **Amazon WorkDocs SDK** - SDK for WorkDocs

### Management
7. **AWS Service Management Connector** - ITSM connector

### Media
8. **AWS Deadline Cloud** - Render farm service (legitimate service)

### Migration
9. **AWS Data Transfer Terminal** - Physical device
10. **AWS Migration Evaluator** - Assessment tool
11. **AWS Transform** - Mainframe migration (legitimate service)

### Security
12. **AWS Private Certificate Authority** - Part of Certificate Manager
13. **AWS Signer** - Code signing service
14. **AWS Payment Cryptography** - Payment HSM service
15. **AWS Security Incident Response** - Incident response service
16. **Amazon Cloud Directory** - Legacy directory service

### Storage
17. **AWS Snowball** - Data transfer device
18. **AWS Snowball Edge** - Compute-enabled Snowball
19. **Amazon FSx for WFS** - Duplicate of FSx for Windows File Server
20. **Amazon S3 on Outposts** - S3 variant
21. **Amazon S3 Glacier** - Storage class vs service

### Financial
22. **Reserved Instance Reporting** - Cost management feature

### Integration
23. **AWS Express Workflows** - Step Functions variant

### Compute
24. **Amazon Elastic VMware Service** - VMware cloud variant
25. **Amazon Lightsail for Research** - Lightsail variant

---

## Summary of Recommendations

| Category | Count | Action |
|----------|-------|--------|
| Already Handled | 6 | ✅ Done |
| Clear Additions | 28 | ➕ Add as new services |
| Granularity Questions | 20 | ❓ Need user decisions |
| Infrastructure/Tooling | 12 | ⛔ Skip |
| Customer Enablement | 6 | ⛔ Skip |
| Service Variants | 15 | 🔍 Evaluate individually |

---

## Recommended Actions

### Immediate Additions (28 services)
Add these as standalone services with full definitions:
- AWS Glue DataBrew, Kinesis (parent), SageMaker (parent)
- Amazon Nova, HealthImaging, HealthOmics, Neuron, Elastic Inference
- Amazon QLDB
- AWS Supply Chain, End User Messaging, Wickr
- AWS Local Zones, Nitro Enclaves, Outposts family, Parallel Computing Service, SimSpace Weaver, Bottlerocket, Elastic Fabric Adapter, NICE EnginFrame
- AWS Chatbot, Resilience Hub, Resource Explorer, Telco Network Builder
- AWS Cloud WAN, Application Recovery Controller

### Service Variants to Consider (8 services)
These may warrant addition depending on user needs:
- AWS Deadline Cloud (Media rendering)
- AWS Transform (Mainframe migration)
- AWS Signer (Code signing)
- AWS Payment Cryptography (Payment HSM)
- AWS Security Incident Response
- Amazon Cloud Directory (Legacy, may skip)
- Alexa For Business (Different from Skills Kit)
- ECS Anywhere / EKS Anywhere (On-prem variants)

### Skip (38 icons)
- Infrastructure tools: 12
- Customer enablement: 6
- ML frameworks: 3
- Deep learning artifacts: 2
- Container distros: 2
- Sub-components: 13

---

## Next Steps

1. Get user confirmation on 28 "Clear Additions"
2. Resolve 8 "Service Variants" questions
3. Confirm decisions on 20 "Granularity Questions"
4. Begin adding approved services with full definitions
