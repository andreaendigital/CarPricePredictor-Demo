# 🚀 Car Price Prediction Platform

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#2563eb', 'primaryTextColor': '#ffffff', 'lineColor': '#374151'}}}%%

flowchart TD
    P["🚗 Car Price Prediction<br/><b>Enterprise ML Platform</b>"]

    subgraph TECH ["🛠️ Technology Stack"]
        T1["🏗️ Terraform"]
        T2["⚙️ Ansible"]
        T3["🔄 Jenkins"]
        T4["☁️ Splunk"]
    end

    subgraph CAPABILITIES ["🎯 Core Capabilities"]
        C1["🧠 ML Intelligence"]
        C2["🏢 Enterprise Ops"]
        C3["🚀 DevOps Excellence"]
    end

    subgraph IMPACT ["💼 Business Impact"]
        I1["⚡ Real-time Decisions"]
        I2["📊 Strategic Planning"]
        I3["🎯 99.9% Reliability"]
    end

    P --> TECH
    TECH --> CAPABILITIES
    CAPABILITIES --> IMPACT

    classDef platform fill:#e3f2fd,stroke:#1976d2,stroke-width:3px
    classDef tech fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef capabilities fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    classDef impact fill:#e0f2f1,stroke:#00695c,stroke-width:3px

    class P platform
    class T1,T2,T3,T4 tech
    class C1,C2,C3 capabilities
    class I1,I2,I3 impact
```

**Development Excellence:**

- **🧠 Advanced ML Engineering** - Production-ready XGBoost models with real-time inference capabilities
- **🏢 Enterprise Observability** - Comprehensive monitoring architecture with high-frequency metrics collection
- **🚀 Modern DevOps Practices** - Full automation pipeline from infrastructure to deployment
- **🌟 Cloud-Native Architecture** - Scalable, containerized microservices on AWS infrastructure

---



## 🏗️ Enterprise Architecture Overview

=== "Interactive Diagram"

    ```mermaid
    %%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#2563eb', 'primaryTextColor': '#ffffff', 'lineColor': '#374151'}}}%%

    flowchart LR
        subgraph SC ["🏛️ SOURCE CONTROL LAYER"]
            direction TB
            A["🏗️ Infrastructure<br/><b>Terraform IaC</b><br/><small>AWS Resources</small>"]
            B["⚙️ Configuration<br/><b>Ansible Automation</b><br/><small>System Setup</small>"]
            C["🚀 Application<br/><b>Flask + XGBoost</b><br/><small>ML Platform</small>"]
        end

        subgraph DP ["🔄 DEPLOYMENT PIPELINE"]
            D["🎯 Jenkins CI/CD<br/><b>Orchestration Engine</b><br/><small>Automated Deployment</small>"]
        end

        subgraph AWS ["☁️ AWS CLOUD INFRASTRUCTURE"]
            direction TB
            E["🌐 VPC Network<br/><b>Security & Isolation</b><br/><small>10.0.0.0/16</small>"]
            F["💻 EC2 Instance<br/><b>Application Runtime</b><br/><small>t3.small</small>"]
            G["📦 S3 Storage<br/><b>State Management</b><br/><small>Terraform Backend</small>"]
        end

        subgraph OBS ["📊 OBSERVABILITY PLATFORM"]
            direction TB
            H["📈 OpenTelemetry<br/><b>Metrics Collection</b><br/><small>Real-time Data</small>"]
            I["☁️ Splunk Cloud<br/><b>Enterprise Monitoring</b><br/><small>High-frequency metrics</small>"]
        end

        A -.->|"Infrastructure Code"| D
        B -.->|"Configuration Scripts"| D
        C -.->|"Application Code"| D

        D ==>|"Provisions"| E
        D ==>|"Deploys"| F
        D ==>|"Manages"| G

        F ==>|"Streams Metrics"| H
        H ==>|"Exports Data"| I

        classDef sourceControl fill:#e3f2fd,stroke:#1976d2,stroke-width:3px
        classDef deployment fill:#f3e5f5,stroke:#7b1fa2,stroke-width:3px
        classDef aws fill:#e8f5e8,stroke:#388e3c,stroke-width:3px
        classDef observability fill:#fff3e0,stroke:#f57c00,stroke-width:3px

        class A,B,C sourceControl
        class D deployment
        class E,F,G aws
        class H,I observability
    ```

=== "AWS RBAC Security"

    ```mermaid
    %%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#2563eb', 'primaryTextColor': '#ffffff', 'lineColor': '#374151'}}}%%

    flowchart TD
        subgraph Users
            U3(👤 seba)
            U1(👤 andrea)
            U2(👤 jose)
            U4(⚙️ terraform-user)
        end

        subgraph IAM Groups
            G1[👥 Group: devops]
            G2[👥 Group: dev]
            G3[⚙️ Group: terraform-service]
        end

        subgraph AWS Permissions Roles
            P1(Policy: PowerUserAccess + IAMReadOnly)
            P2(Policy: Developer/Read-Only)
        end

        U1 --> G1
        U2 --> G1
        U3 --> G2
        U4 --> G3

        G1 --> P1
        G3 --> P1
        G2 --> P2

        classDef users fill:#e3f2fd,stroke:#1976d2,stroke-width:3px
        classDef groups fill:#f3e5f5,stroke:#7b1fa2,stroke-width:3px
        classDef policies fill:#e8f5e8,stroke:#388e3c,stroke-width:3px
        classDef service fill:#fff3e0,stroke:#f57c00,stroke-width:3px

        class U1,U2,U3 users
        class U4 service
        class G1,G2,G3 groups
        class P1,P2 policies
    ```

    **Security Architecture:**

    - **Role Separation** - Human users (andrea, jose, seba) and service accounts (terraform-user) have **distinct access patterns**
    - **Group-Based Permissions** - DevOps team gets PowerUserAccess, developers get read-only access for **principle of least privilege**
    - **Service Isolation** - Terraform service user has dedicated group for **auditable infrastructure operations**
    - **Policy Management** - Centralized IAM policies ensure **consistent security controls** across all environments

=== "Architecture AWS"

    ![AWS Architecture](../assets/images/18.jpeg)

    *Complete AWS infrastructure architecture showing VPC networking, EC2 compute instances, security groups, load balancers, and integrated monitoring components for the Car Price Prediction Platform.*

**Architecture Flow:**

- **Three-Repository Structure** - Infrastructure, Configuration, and Application repositories provide **separation of concerns**
- **Jenkins CI/CD Orchestration** - Automated pipeline manages **end-to-end deployment** across all environments
- **AWS Cloud Infrastructure** - VPC, EC2, and S3 deliver **enterprise-grade hosting** with security isolation
- **Comprehensive Observability** - OpenTelemetry collectors stream **real-time metrics** to Splunk Cloud for analytics
- **Enterprise Security** - Role-based access control ensures **secure operations** with proper user and service account separation

---

<div style="text-align: center; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 20px; border-radius: 10px; margin: 20px 0; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
<h1 style="margin: 0; font-size: 2.2em; font-weight: bold;">📊 PART II: OBSERVABILITY & MONITORING FRAMEWORK</h1>
<p style="margin: 10px 0 0 0; font-size: 1.1em; opacity: 0.9;">Splunk Cloud • High-frequency Metrics • Real-time Dashboards</p>
</div>

---

## 🔄 Deployment Flow

=== "Interactive Diagram"

    ```mermaid
    flowchart LR
        subgraph "Pipeline Execution"
            A[🚀 Jenkins<br/>Orchestration]
            B[🏗️ Terraform<br/>Infrastructure]
            C[⚙️ Ansible<br/>Configuration]
            D[🎯 Health<br/>Validation]
        end

        subgraph "Infrastructure Layer"
            E[🌐 AWS VPC<br/>Network Isolation]
            F[💻 EC2 t3.small<br/>Compute Instance]
            G[📦 S3 Bucket<br/>State Management]
            H[🔒 Security Groups<br/>Access Control]
        end

        subgraph "Application Layer"
            I[🐍 Flask Services<br/>systemd Deployment]
            J[🔧 Python Environment<br/>Dependencies Setup]
        end

        subgraph "Monitoring Layer"
            K[📊 OpenTelemetry<br/>Collector Installation]
            L[☁️ Splunk Integration<br/>Observability Cloud]
        end

        A --> B
        B --> C
        C --> D

        B --> E
        B --> F
        B --> G
        B --> H

        C --> I
        C --> J
        C --> K

        K --> L

        D --> M[✅ Backend :5002<br/>Health Check]
        D --> N[✅ Frontend :3000<br/>Health Check]

        style A fill:#e1f5fe
        style D fill:#c8e6c9
        style L fill:#e8f5e8
    ```

=== "PR Example"

    ```markdown
    ## Pull Request: SCRUM-95 - Add Real-time Monitoring Dashboard

    ### 📋 Description
    Implements comprehensive monitoring dashboard with live metrics collection and Splunk integration for the Car Price Prediction Platform.

    ### 🔧 Changes Made
    - ✅ Added real-time dashboard endpoint (`/dashboard`)
    - ✅ Integrated OpenTelemetry metrics collection
    - ✅ Configured Splunk Observability Cloud streaming
    - ✅ Implemented 5-second auto-refresh functionality
    - ✅ Added system health monitoring (CPU, Memory, Uptime)

    ### 🧪 Testing
    - [x] Unit tests for dashboard endpoints
    - [x] Integration tests with Splunk API
    - [x] Load testing for metrics collection
    - [x] Cross-browser compatibility testing

    ### 📊 Metrics Impact
    - **Before**: No real-time monitoring
    - **After**: 1,070+ metrics/hour streaming to Splunk Cloud

    ### 🚀 Deployment Notes
    - Requires Splunk token configuration
    - Auto-deploys via Jenkins CI/CD pipeline
    - Health checks validate service connectivity

    ### 📸 Screenshots
    ![Dashboard Preview](../assets/images/photo3.png)

    **Reviewers**: @andrea @jose
    **JIRA**: [SCRUM-95](https://jira.company.com/browse/SCRUM-95)
    ```

    *Example pull request demonstrating professional development workflow with comprehensive testing, metrics impact analysis, and deployment considerations for the monitoring dashboard feature.*

=== "Jenkins Pipeline Code"

    <div style="font-size: 0.7em; font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace; line-height: 1.3; background: #1e1e1e; border-radius: 8px; padding: 12px; overflow-x: auto; color: #d4d4d4;">

    ```groovy
    pipeline {
      agent any
      parameters {
        booleanParam(name: 'PLAN_TERRAFORM', defaultValue: true, description: 'Run terraform plan')
        booleanParam(name: 'APPLY_TERRAFORM', defaultValue: true, description: 'Apply infrastructure')
        booleanParam(name: 'DEPLOY_ANSIBLE', defaultValue: true, description: 'Deploy Flask app')
        booleanParam(name: 'DESTROY_TERRAFORM', defaultValue: false, description: 'Destroy infra')
      }
      environment {
        ANSIBLE_DIR = 'configManagement-carPrice'
        INVENTORY_SCRIPT = "${ANSIBLE_DIR}/generate_inventory.sh"
        INVENTORY_FILE = "${ANSIBLE_DIR}/inventory.ini"
        PLAYBOOK_FILE = "${ANSIBLE_DIR}/playbook.yml"
      }
      stages {
        stage('Clone Repositories') {
          steps {
            echo 'Cleaning workspace and cloning repositories...'
            deleteDir()
            git branch: 'main', url: 'https://github.com/andreaendigital/tf-infra-demoCar'
            dir("${ANSIBLE_DIR}") {
              checkout([$class: 'GitSCM', branches: [[name: 'main']],
                       userRemoteConfigs: [[url: 'https://github.com/andreaendigital/configManagement-carPrice']]])
            }
          }
        }
        stage('Terraform Init') {
          steps {
            withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-jenkins-carprice']]) {
              dir('infra') { sh 'export AWS_PROFILE=""'; sh 'terraform init' }
            }
          }
        }
        stage('Terraform Plan') {
          when { expression { return params.PLAN_TERRAFORM } }
          steps {
            withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-jenkins-carprice']]) {
              dir('infra') { sh 'terraform plan -out=tfplan' }
            }
          }
        }
        stage('Terraform Apply') {
          when { expression { return params.APPLY_TERRAFORM } }
          steps {
            withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-jenkins-carprice']]) {
              dir('infra') { sh 'terraform apply -auto-approve tfplan' }
            }
          }
        }
        stage('Terraform Destroy') {
          when { expression { return params.DESTROY_TERRAFORM } }
          steps {
            withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-jenkins-carprice']]) {
              dir('infra') { sh 'terraform destroy -auto-approve' }
            }
          }
        }
        stage('Generate Ansible Inventory') {
          when { expression { return params.DEPLOY_ANSIBLE } }
          steps {
            withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-jenkins-carprice']]) {
              sh "chmod +x ${INVENTORY_SCRIPT}"; sh "${INVENTORY_SCRIPT}"
            }
          }
        }
        stage('Run Ansible Playbook') {
          when { expression { return params.DEPLOY_ANSIBLE } }
          steps {
            sshagent(credentials: ['ansible-ssh-key']) {
              sh "ansible-playbook -i ${INVENTORY_FILE} ${PLAYBOOK_FILE} --extra-vars 'ansible_ssh_common_args=\"-o StrictHostKeyChecking=no\"'"
            }
          }
        }
      }
      post {
        success {
          script {
            sh '''
              curl -X POST https://ingest.us1.signalfx.com/v2/datapoint \
              -H "X-SF-Token: PZuf3J0L2Op_Qj9hpAJzlw" \
              -H "Content-Type: application/json" \
              -d '{"gauge":[{"metric":"jenkins.pipeline.success","value":1,"dimensions":{"job":"''' + env.JOB_NAME + '''","build":"''' + env.BUILD_NUMBER + '''","result":"success"}}]}'
            '''
          }
          echo 'Deployment completed successfully!'
        }
        failure {
          script {
            sh '''
              curl -X POST https://ingest.us1.signalfx.com/v2/datapoint \
              -H "X-SF-Token: PZuf3J0L2Op_Qj9hpAJzlw" \
              -H "Content-Type: application/json" \
              -d '{"gauge":[{"metric":"jenkins.pipeline.failure","value":1,"dimensions":{"job":"''' + env.JOB_NAME + '''","build":"''' + env.BUILD_NUMBER + '''","result":"failure"}}]}'
            '''
          }
          echo 'Deployment failed. Check logs and Terraform state.'
        }
      }
    }
    ```

    </div>

    *Complete Jenkins pipeline implementing Infrastructure as Code with Terraform, configuration management with Ansible, and Splunk observability integration.*

=== "Terraform Workflow"

    ```mermaid
    %%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#2563eb', 'primaryTextColor': '#ffffff', 'lineColor': '#374151'}}}%%

    flowchart TD
         subgraph Repo ["tf-infra-demoCar"]
            direction TB
            A["main.tf <br/><b>Orchestration Layer</b><br/><small>Calls all modules</small>"]
            B["remote_backend_s3.tf <br/><b>Remote State Config</b>"]
            C["variables.tf / terraform.tfvars <br/><b>Input Customization</b>"]
        end

        subgraph IaC ["infra/ Modules"]
            direction LR
            M1["networking/<br/><b>VPC, Subnets</b>"]
            M2["security-groups/<br/><b>Firewall Rules</b>"]
            M3["ec2/<br/><b>Compute Instance</b>"]
            M4["rds/<br/><b>DB Deployment</b>"]
            M5["load-balancer/<br/><b>ALB Setup</b>"]
            M6["load-balancer-target-group/<br/><b>Traffic Routing</b>"]
            M7["s3/<br/><b>State Backend</b>"]
        end

        AWS["☁️ AWS Cloud<br/><b>Deployed Resources</b>"]
        S3["📦 AWS S3/DynamoDB<br/><b>Remote State Locking</b>"]

        A --> M1
        M1 --> M2
        M1 --> M3
        M1 --> M5
        M3 --> M6
        M4 --> M2
        B --> M7
        A --> AWS
        B --> S3

        classDef main fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
        classDef module fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
        classDef remote fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
        classDef cloud fill:#fff3e0,stroke:#f57c00,stroke-width:2px

        class A,C main
        class M1,M2,M3,M4,M5,M6,M7 module
        class B,M7 remote
        class AWS,S3 cloud
    ```

    *Terraform architecture based on local-per-service module pattern to manage infrastructure complexity. The main.tf file acts as central orchestration layer, focusing on invoking and passing variables to each specialized module.*

=== "Architecture Image"

    ![Enterprise Architecture](../assets/images/photo1.png){: style="width: 60%; height: auto; display: block; margin: 0 auto;"}

    *Professional visualization of the complete enterprise architecture with AWS cloud infrastructure, CI/CD pipeline, and observability platform.*

=== "Ansible Workflow"

    ```mermaid
    %%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#2563eb', 'primaryTextColor': '#ffffff', 'lineColor': '#374151'}}}%%

    flowchart TD
        A["Jenkins Ansible Stage"]
        B["Generate Dynamic Inventory"]
        C["EC2 Target Host"]

        subgraph ROLES ["Ansible Roles"]
            D["Flask App Setup"]
            E["Splunk Monitoring"]
        end

        subgraph TASKS ["Task Execution"]
            F["Install Dependencies"]
            G["Configure Services"]
            H["Start Applications"]
        end

        I["Deployment Complete"]

        A --> B
        B --> C
        C --> ROLES
        D --> TASKS
        E --> TASKS
        F --> G
        G --> H
        H --> I

        classDef main fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
        classDef roles fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
        classDef tasks fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
        classDef complete fill:#fff3e0,stroke:#f57c00,stroke-width:2px

        class A,B,C main
        class D,E roles
        class F,G,H tasks
        class I complete
    ```

    *The Dynamic Inventory step is crucial: because we're working with a dynamic IP address for the EC2 instance (a common setup in the free tier), the generate_inventory.sh script is indispensable. This script resolves the coupling by programmatically extracting the IP address from the Terraform output, creating the inventory.ini file that Ansible requires.*

=== "PlatOps Pipeline"

    ```mermaid
    %%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#2563eb', 'primaryTextColor': '#ffffff', 'lineColor': '#374151'}}}%%

    flowchart TD
        subgraph PlatOps
            direction TB
            L1[🚀 Jenkins CI/CD<br/>Orchestration & Self-Service]
            L2[🏗️ Terraform Modules<br/><b>Standardized Infrastructure</b>]
            L3[⚙️ Ansible Roles<br/><b>Abstracted Configuration</b>]
            L4[📊 Observability Stack<br/><b>Integrated Metrics</b>]
        end

        A[Car Price Predictor Demo <br/> -Flask/XGBoost App-]

        A --> L1
        L1 --> L2
        L1 --> L3
        L1 --> L4
        L4 --> O[Operational Readiness]

        classDef platform fill:#e3f2fd,stroke:#1976d2,stroke-width:3px
        classDef dev fill:#f3e5f5,stroke:#7b1fa2,stroke-width:3px
        classDef ops fill:#e8f5e8,stroke:#388e3c,stroke-width:3px

        class L1,L2,L3,L4 platform
        class A dev
        class O ops
    ```

    *As a team, we understand PlatOps as the evolution of DevOps focused on building and maintaining an Internal Developer Platform (IDP). While DevOps focuses on CI/CD practices, PlatOps focuses on the Platform team that builds the tooling, pipelines, templates, and infrastructure so that teams can focus on the application code. This is achieved through Infrastructure as a Product: our Terraform modules are not one-time-use scripts, but standardized building blocks (ec2/, rds/). The Jenkins pipeline acts as a self-service deployment API that abstracts the complexity, orchestrating Terraform, Ansible, and the telemetry configuration for sending metrics to the Splunk cloud.*

**Deployment Process:**

- **Jenkins Orchestration** - Central pipeline manages **automated deployment** across all infrastructure layers
- **Terraform Provisioning** - Infrastructure as Code creates **AWS resources** (VPC, EC2, S3, Security Groups)
- **Ansible Configuration** - Automated setup deploys **Flask services** with Python dependencies
- **OpenTelemetry Integration** - Collectors installed for **real-time metrics** streaming to Splunk Cloud
- **Health Validation** - Automated checks verify **backend and frontend** services before completion

---

## 📊 Enterprise Observability Framework

=== "Telemetry Architecture"

    ```
    ┌─────────────────────────────────────────────────────────────────┐
    │                    SPLUNK OBSERVABILITY CLOUD                  │
    │                     Enterprise Monitoring Platform              │
    └─────────────────────────────────────────────────────────────────┘
                                        ▲
                                        │ Metrics & Telemetry
                        ┌───────────────┼───────────────┐
                        │               │               │
                ┌───────▼──────┐ ┌──────▼──────┐ ┌─────▼─────┐
                │ Application  │ │Infrastructure│ │ Pipeline  │
                │   Layer      │ │   Layer      │ │  Layer    │
                │              │ │              │ │           │
                │ • Backend    │ │ • EC2 Metrics│ │ • Jenkins │
                │ • Frontend   │ │ • CPU/Memory │ │ • Terraform│
                │ • ML Models  │ │ • Network    │ │ • Ansible │
                │ • Business   │ │ • Disk Usage │ │ • Health  │
                │   KPIs       │ │ • System     │ │   Checks  │
                └──────────────┘ └─────────────┘ └───────────┘
                        │               │               │
                ┌───────▼──────┐ ┌──────▼──────┐ ┌─────▼─────┐
                │ OpenTelemetry│ │HostMetrics  │ │ Jenkins   │
                │ Collector    │ │ Collector   │ │ Pipeline  │
                │ (Port 3000)  │ │ (10s int.)  │ │ Metrics   │
                │ (Port 5002)  │ │             │ │           │
                └──────────────┘ └─────────────┘ └───────────┘

    ```

    **Telemetry Flow:**

    - **Three-Layer Architecture** - Application, Infrastructure, and Pipeline layers provide **comprehensive coverage**
    - **Specialized Collectors** - OpenTelemetry, HostMetrics, and Jenkins collectors ensure **targeted data capture**
    - **Enterprise Platform** - Splunk Observability Cloud delivers **centralized monitoring** and analytics
    - **Real-Time Streaming** - Continuous metrics flow enables **proactive operational management**

=== "Observability Image"

    ![Enterprise Observability](../assets/images/photo2.png)

    *Complete observability framework with Splunk Cloud integration, multi-layer telemetry collection, and enterprise-grade monitoring capabilities.*

<div style="text-align: center; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; padding: 20px; border-radius: 10px; margin: 20px 0; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
<h1 style="margin: 0; font-size: 2.2em; font-weight: bold;">🚀 PART III: DEPLOYMENT & OPERATIONS</h1>
<p style="margin: 10px 0 0 0; font-size: 1.1em; opacity: 0.9;">Production Environment • Health Monitoring • Access Points</p>
</div>

---

### Data Collection Flow

=== "Interactive Diagram"

    ```mermaid
    %%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#2563eb', 'primaryTextColor': '#ffffff'}}}%%

    flowchart LR
        subgraph SOURCES ["📊 DATA SOURCES"]
            direction TB
            S1["🖥️ Backend App<br/><b>~360/hour</b><br/><small>30s interval</small>"]
            S2["🌐 Frontend App<br/><b>~360/hour</b><br/><small>30s interval</small>"]
            S3["🏗️ EC2 Infrastructure<br/><b>~200/hour</b><br/><small>10s interval</small>"]
            S4["🔧 Jenkins Pipeline<br/><b>~50/deployment</b><br/><small>Per build</small>"]
            S5["☁️ AWS Resources<br/><b>~100/hour</b><br/><small>60s interval</small>"]
        end

        subgraph COLLECTORS ["🔄 COLLECTION LAYER"]
            direction TB
            C1["📈 OpenTelemetry<br/><b>App Metrics</b>"]
            C2["📊 HostMetrics<br/><b>System Data</b>"]
            C3["🔄 Pipeline<br/><b>DevOps Metrics</b>"]
        end

        subgraph PROCESSING ["⚙️ PROCESSING"]
            direction TB
            P1["🔍 Resource Detection<br/><b>Auto-discovery</b><br/><small>Service identification</small>"]
            P2["🏷️ Attribute Processing<br/><b>Data Enrichment</b><br/><small>Metadata tagging</small>"]
            P3["📤 Splunk Export<br/><b>Real-time Stream</b><br/><small>Enterprise delivery</small>"]
        end

        subgraph ANALYTICS ["📊 ANALYTICS PLATFORM"]
            A1["☁️ Splunk Observability<br/><b>High-frequency metrics</b><br/><small>Enterprise Analytics</small>"]
        end

        S1 --> C1
        S2 --> C1
        S3 --> C2
        S4 --> C3
        S5 --> C2

        C1 --> P1
        C2 --> P1
        C3 --> P1

        P1 --> P2
        P2 --> P3
        P3 --> A1

        classDef sources fill:#e3f2fd,stroke:#1976d2,stroke-width:3px
        classDef collectors fill:#f3e5f5,stroke:#7b1fa2,stroke-width:3px
        classDef processing fill:#e8f5e8,stroke:#388e3c,stroke-width:3px
        classDef analytics fill:#fff3e0,stroke:#f57c00,stroke-width:3px

        class S1,S2,S3,S4,S5 sources
        class C1,C2,C3 collectors
        class P1,P2,P3 processing
        class A1 analytics
    ```

=== "Splunk Collection Code"

    <div style="font-size: 0.7em; font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace; line-height: 1.3; background: #1e1e1e; border-radius: 8px; padding: 12px; overflow-x: auto; color: #d4d4d4;">

    ```python
    # Frontend Prediction Metrics Collection (car_price.frontend.predictions)

    @app.route("/predict", methods=["POST"])
    def predict():
        global prediction_requests
        prediction_requests += 1

        # Send metrics to Splunk Observability Cloud
        send_to_splunk_observability(
            "car_price.frontend.predictions", 1,
            {"user_ip": request.remote_addr or "unknown", "action": "current_prediction"}
        )
        send_to_splunk_observability("car_price.frontend.requests.total", prediction_requests)

    def send_to_splunk_observability(metric_name, value, dimensions=None):
        """Send metrics to Splunk Observability Cloud"""
        try:
            headers = {"X-SF-Token": SPLUNK_TOKEN, "Content-Type": "application/json"}

            if dimensions is None: dimensions = {}

            # Add default dimensions
            dimensions.update({
                "service": "car-price-frontend",
                "environment": "development",
                "host": "localhost"
            })

            payload = {
                "gauge": [{
                    "metric": metric_name,
                    "value": value,
                    "dimensions": dimensions,
                    "timestamp": int(time.time() * 1000)
                }]
            }

            response = requests.post(SPLUNK_URL, json=payload, headers=headers, timeout=5)
            if response.status_code != 200:
                print(f"❌ Splunk error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"❌ Splunk error: {e}")

    # Continuous Metrics Collection (every 10 seconds)
    def send_continuous_metrics():
        while continuous_monitoring:
            try:
                send_to_splunk_observability("car_price.frontend.cpu_percent", psutil.cpu_percent())
                send_to_splunk_observability("car_price.frontend.memory_percent", psutil.virtual_memory().percent)
                send_to_splunk_observability("car_price.frontend.uptime_seconds", time.time() - start_time)
                send_to_splunk_observability("car_price.frontend.total_requests", request_count)
                send_to_splunk_observability("car_price.frontend.prediction_requests", prediction_requests)
                time.sleep(10)  # Send metrics every 10 seconds
            except Exception as e:
                print(f"❌ Frontend continuous metrics error: {e}")
    ```

    </div>

    *Real-time metrics collection showing how `car_price.frontend.predictions` and other business metrics are captured and streamed to Splunk Observability Cloud with user context and dimensional data.*

**Data Collection Process:**

- **Multiple Data Sources** - Backend/Frontend apps, EC2 infrastructure, Jenkins pipeline generate **diverse metrics**
- **Specialized Collectors** - OpenTelemetry, HostMetrics, and Pipeline collectors provide **targeted monitoring**
- **Unified Processing** - Resource detection and attribute processing ensure **data consistency**
- **Splunk Integration** - Real-time export delivers **high-frequency metrics collection** for enterprise analytics
- **Comprehensive Visibility** - Complete platform monitoring from **application to infrastructure**

### Implemented Metrics

=== "Metrics Volume"

    | Layer | Component | Metrics/Hour | Collection Interval |
    |-------|-----------|--------------|--------------------|
    | **Application** | Backend Service | ~360 | 30 seconds |
    | **Application** | Frontend Service | ~360 | 30 seconds |
    | **Infrastructure** | EC2 Host Metrics | ~200 | 10 seconds |
    | **Pipeline** | Jenkins Deployment | ~50 | Per deployment |
    | **Cloud** | AWS Resources | ~100 | 60 seconds |
    | **Total** | **Enterprise Platform** | **High-volume** | **Real-time** |

=== "Backend Metrics"

    | Metric Name | Description | Type |
    |-------------|-------------|------|
    | `car_price.app.total_predictions` | ML predictions made | Business |
    | `car_price.system.cpu_percent` | System CPU usage | Performance |
    | `car_price.app.uptime_seconds` | Application uptime | Availability |
    | `car_price.predictions.current_value` | Current price predictions | Business |
    | `car_price.predictions.future_value` | Future price predictions | Business |

=== "Frontend Metrics"

    | Metric Name | Description | Type |
    |-------------|-------------|------|
    | `car_price.frontend.predictions` | User prediction actions | Business |
    | `car_price.frontend.total_requests` | Web requests | Usage |
    | `car_price.frontend.uptime_seconds` | Frontend uptime | Availability |
    | `car_price.frontend.prediction_requests` | Prediction requests | Business |
    | `car_price.frontend.cpu_percent` | Frontend CPU usage | Performance |

=== "Pipeline Metrics"

    | Metric Name | Description | Type |
    |-------------|-------------|------|
    | `jenkins.pipeline.success` | Pipeline success results | DevOps |
    | `jenkins.pipeline.failure` | Pipeline failure results | DevOps |
    | `jenkins.terraform.apply.duration` | Infrastructure deployment time | DevOps |
    | `jenkins.ansible.deploy.duration` | Configuration deployment time | DevOps |
    | `ansible.deployment.success` | Configuration success | DevOps |

---

## 📊 Available Dashboards

=== "Interactive Diagram"

    ```mermaid
    %%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#2563eb', 'primaryTextColor': '#ffffff'}}}%%

    flowchart LR
        subgraph USERS ["👥 TARGET USERS"]
        direction TB

        U2["🔧 Operations<br/><small>System Health</small>"]
        U3["👨‍💻 Developers<br/><small>Technical Metrics</small>"]
    end

    subgraph LOCAL ["🖥️ LOCAL DASHBOARDS"]
        direction TB
        L1["🎨 Frontend Dashboard<br/><b>Port 3000/dashboard</b><br/><small>• User Activity<br/>• Page Performance<br/>• 5s Auto-refresh</small>"]
        L2["🔌 Backend Dashboard<br/><b>Port 5002/dashboard</b><br/><small>• API Performance<br/>• ML Predictions<br/>• System Health</small>"]
    end

    subgraph ENTERPRISE ["☁️ ENTERPRISE PLATFORM"]
        direction TB
        E1["📊 Splunk Observability<br/><b>app.us1.signalfx.com</b><br/><small>• High-frequency metrics<br/>• 30-day retention<br/>• Custom dashboards<br/>• Real-time alerts</small>"]
    end

    subgraph ANALYTICS ["📈 ANALYTICS VIEWS"]
        direction TB

        A2["🎯 Operational View<br/><small>Performance & SLA</small>"]
        A3["🔍 Technical View<br/><small>Infrastructure & Code</small>"]
    end


    L1 ==> E1
    L2 ==> E1
    E1 ==> A2
    E1 ==> A3
    A2 -.-> U2
    A3 -.-> U3

    classDef users fill:#fef3c7,stroke:#f59e0b,stroke-width:3px
    classDef local fill:#e3f2fd,stroke:#1976d2,stroke-width:3px
    classDef enterprise fill:#f3e5f5,stroke:#7b1fa2,stroke-width:3px
    classDef analytics fill:#e8f5e8,stroke:#388e3c,stroke-width:3px

    class U2,U3 users
    class L1,L2 local
    class E1 enterprise
    class A2,A3 analytics
    ```

=== "Backend Dashboard Image"

    ![Backend Dashboard](../assets/images/photo3.png)

    *Backend monitoring dashboard showing API performance, ML predictions, system health metrics, and real-time service status with 5-second auto-refresh.*

=== "Frontend Dashboard Image"

    ![Frontend Dashboard](../assets/images/photo4.png)

    *Frontend monitoring dashboard showing user activity, web metrics, system performance, and real-time interaction tracking with live updates.*

=== "Splunk Example"

    ![Splunk Example](../assets/images/photo5.png)

    *Splunk Observability Cloud dashboard showing enterprise-grade monitoring with 1,070+ metrics per hour, real-time analytics, and comprehensive system visibility.*

**Dashboard Ecosystem:**

- **Multi-Tier Visibility** - Local dashboards provide **application-level insights** for Backend and Frontend services
- **Real-Time Processing** - Unified data flow ensures **live metric collection** and processing
- **Dual Visualization** - Local interfaces and **Splunk Observability** platform offer comprehensive views
- **Enterprise Analytics** - Complete operational awareness from **granular details to strategic insights**
- **Operational Excellence** - Continuous monitoring enables **proactive management** and optimization

=== "Backend Dashboard"

    **Access**: Port 5002/dashboard | **URL**: http://13.220.64.167:5002/dashboard

    | Feature | Description | Update Frequency |
    |---------|-------------|------------------|
    | **System Metrics** | CPU, Memory, Uptime | Real-time |
    | **API Performance** | Total requests, ML predictions | Live tracking |
    | **Real-time Updates** | Auto-refresh dashboard | Every 5 seconds |
    | **Splunk Integration** | Direct link to observability platform | On-demand |

=== "Frontend Dashboard"

    **Access**: Port 3000/dashboard | **URL**: http://13.220.64.167:3000/dashboard

    | Feature | Description | Update Frequency |
    |---------|-------------|------------------|
    | **Web Metrics** | User requests, predictions, publishes | Real-time |
    | **System Performance** | CPU, Memory usage | Live monitoring |
    | **User Activity** | Real-time interaction tracking | Instant |
    | **Health Status** | Service connectivity monitoring | Continuous |

=== "Splunk Observability"

    **Access**: Enterprise Platform | **URL**: https://app.us1.signalfx.com

    | Feature | Description | Capability |
    |---------|-------------|------------|
    | **Comprehensive Metrics** | High-frequency collection | Enterprise scale |
    | **Real-time Visualization** | Live data streaming | Instant insights |
    | **Historical Analysis** | 30-day data retention | Trend analysis |
    | **Custom Dashboards** | Business and technical KPIs | Configurable views |



---

## 🔧 Deployment Commands

=== "Infrastructure Deployment"

    | Step | Command | Description |
    |------|---------|-------------|
    | **1. Deploy Infrastructure** | `cd terraform`<br/>`terraform init`<br/>`terraform plan`<br/>`terraform apply` | Initialize and deploy AWS infrastructure |
    | **2. Configure Monitoring** | `cd ../ansible`<br/>`ansible-playbook -i inventory splunk-observability.yml` | Setup Splunk observability collectors |
    | **3. Deploy Application** | `ansible-playbook -i inventory deploy-app.yml` | Deploy Flask ML application |
    | **4. Verify Monitoring** | `curl http://13.220.64.167:5002/health`<br/>`curl http://13.220.64.167:3000/health` | Validate service health |

=== "Access Points"

    | Service | URL | Description |
    |---------|-----|-------------|
    | **Splunk Observability** | https://app.us1.signalfx.com | Enterprise monitoring platform |
    | **Production Application** | http://13.220.64.167:3000/ | Main ML prediction interface |
    | **Backend Dashboard** | http://13.220.64.167:5002/dashboard | API performance monitoring |
    | **Frontend Dashboard** | http://13.220.64.167:3000/dashboard | User activity monitoring |
    | **Backend Health** | http://13.220.64.167:5002/health | Backend service status |
    | **Frontend Health** | http://13.220.64.167:3000/health | Frontend service status |

=== "Implementation Summary"

    | Component | Details | Status |
    |-----------|---------|--------|
    | **Platform Status** | Production-ready ML prediction service with enterprise DevOps architecture | ✅ Active |
    | **Monitoring Coverage** | Application, infrastructure, and pipeline metrics with Splunk Observability Cloud | ✅ Integrated |
    | **Architecture** | 3-repository structure with Terraform IaC, Ansible configuration, and Flask application | ✅ Deployed |
    | **Deployment** | Jenkins CI/CD pipeline with automated AWS provisioning and monitoring integration | ✅ Automated |
    | **Team** | Jose Rubio (Project Lead) \| Full-stack MLOps \| SCRUM methodology | ✅ Operational |

---

*Enterprise DevOps documentation for Car Price Prediction Platform - Complete AWS deployment with comprehensive observability and monitoring.*
