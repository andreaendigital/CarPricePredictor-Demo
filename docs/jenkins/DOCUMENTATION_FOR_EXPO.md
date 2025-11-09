# 🚀 Car Price Prediction Platform - Enterprise DevOps Documentation for Expo

## Executive Summary

**Professional full-stack machine learning platform** for automotive price prediction with enterprise-grade DevOps architecture, comprehensive observability, and modern cloud deployment strategies.

### Business Value
- **Real-time ML Predictions** - Instant vehicle valuations using XGBoost algorithms
- **Enterprise Observability** - 1,070+ metrics per hour with Splunk Observability Cloud
- **Infrastructure as Code** - Complete AWS deployment automation
- **Production-Ready** - High availability, auto-scaling, and comprehensive monitoring

---

## 🏗️ Architecture Overview

```mermaid
graph TB
    subgraph "GitHub Repositories"
        A[tf-infra-demoCar<br/>Infrastructure Code]
        B[configManagement-carPrice<br/>Ansible Configuration]
        C[CarPricePredictor-Demo<br/>Flask Application]
    end

    subgraph "Jenkins CI/CD"
        D[Jenkinsfile<br/>Pipeline Orchestration]
    end

    subgraph "AWS Infrastructure"
        E[VPC + Subnets<br/>Network Layer]
        F[EC2 Instance<br/>Application Server]
        I[S3 Bucket<br/>Terraform State]
    end

    subgraph "Monitoring Stack"
        J[Splunk Observability<br/>Metrics & Dashboards]
        K[OpenTelemetry<br/>Collector]
    end

    A --> D
    B --> D
    D --> E
    D --> F
    D --> I
    C --> F
    F --> K
    K --> J
```

### Repository Architecture

**Infrastructure Repository**: tf-infra-demoCar
```
tf-infra-demoCar/
├── Jenkinsfile                    # CI/CD Pipeline Definition
├── infra/
│   ├── main.tf                   # Main Infrastructure Configuration
│   ├── variables.tf              # Input Variables
│   ├── outputs.tf                # Output Values
│   ├── terraform.tfvars          # Variable Values
│   ├── monitoring.tf             # Observability Integration
│   ├── remote_backend_s3.tf      # Remote State Configuration
│   └── modules/
│       ├── networking/           # VPC, Subnets, Routing
│       ├── security-groups/      # Security Group Rules
│       ├── ec2/                  # EC2 Instance Configuration

│       └── s3/                   # S3 Bucket for State
└── README.md                     # Infrastructure Documentation
```

**Configuration Management Repository**: configManagement-carPrice
```
configManagement-carPrice/
├── playbook.yml                  # Main Ansible Playbook
├── generate_inventory.sh         # Dynamic Inventory Generator
├── inventory.ini                 # Ansible Inventory File
└── roles/
    ├── flask_app/               # Flask Application Role
    │   ├── defaults/main.yml    # Default variables
    │   ├── tasks/main.yml       # Application deployment tasks
    │   └── templates/
    │       ├── app.service.j2   # Backend systemd service
    │       ├── frontend.service.j2 # Frontend systemd service
    │       └── start-production.sh.j2 # Production startup script
    └── splunk_monitoring/       # Monitoring Role
        ├── tasks/main.yml       # OpenTelemetry installation
        ├── templates/
        │   └── agent_config.yaml.j2 # OTel Collector config
        ├── handlers/main.yml    # Service restart handlers
        └── vars/main.yml        # Configuration variables
```

---

## 🔄 Deployment Flow Architecture

### Phase 1: Pipeline Initiation
```
Jenkins Server → Jenkinsfile (tf-infra-demoCar/Jenkinsfile)
├── 1. Clone Repositories
│   ├── tf-infra-demoCar (Infrastructure)
│   └── configManagement-carPrice (Ansible)
├── 2. Terraform Operations
│   ├── terraform init (S3 backend)
│   ├── terraform plan (Preview changes)
│   └── terraform apply (Provision AWS resources)
└── 3. Generate Ansible Inventory
    └── Dynamic EC2 IP discovery
```

### Phase 2: Infrastructure Provisioning
```
AWS Account
├── 🌐 VPC (10.0.0.0/16)
│   ├── Public Subnet (us-east-1a): 10.0.1.0/24
│   └── Public Subnet (us-east-1b): 10.0.2.0/24
├── 🔒 Security Groups
│   ├── SSH Access (Port 22)
│   ├── HTTP/HTTPS (Ports 80, 443)
│   └── Application Ports (3000, 5002)
├── 💻 EC2 Instance (t3.small)
│   ├── Amazon Linux 2
│   ├── Public IP Assignment
│   └── Key Pair Authentication

└── 📦 S3 Bucket
    └── Terraform State Storage
```

### Phase 3: Application Deployment
```
Ansible Playbook Execution
├── 🐍 Flask App Role
│   ├── System package updates
│   ├── Python 3 + pip installation
│   ├── Git repository cloning
│   ├── Virtual environment setup
│   ├── Dependencies installation
│   ├── Systemd service creation
│   │   ├── carprice.service (Backend - Port 5002)
│   │   └── carprice-frontend.service (Frontend - Port 3000)
│   └── Service startup & enablement
└── 📊 Splunk Monitoring Role
    ├── curl package conflict resolution
    ├── OpenTelemetry Collector installation
    ├── Configuration deployment
    │   ├── Host metrics collection
    │   ├── Prometheus scraping (Ports 3000, 5002)
    │   └── Splunk Observability export
    └── Service startup & health check
```

### Phase 4: Monitoring Integration
```
Splunk Observability Cloud (https://app.us1.signalfx.com)
├── 📊 Infrastructure Metrics
│   ├── EC2: CPU, Memory, Disk, Network
├── 🚀 Application Metrics
│   ├── Backend (Port 5002): API performance, ML predictions
│   ├── Frontend (Port 3000): User sessions, page views
│   └── Business KPIs: Revenue tracking, model accuracy
└── 🔧 Pipeline Metrics
    ├── Jenkins: Success/failure rates
    ├── Terraform: Deployment duration
    └── Ansible: Configuration success
```

---

## 📊 Enterprise Observability Framework

### Telemetry Architecture

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

### Data Collection Framework

| Component                | Metrics/Hour | Collection Interval |
| ------------------------ | ------------ | ------------------- |
| **Application Backend**  | ~360         | 30 seconds          |
| **Application Frontend** | ~360         | 30 seconds          |
| **EC2 Infrastructure**   | ~200         | 10 seconds          |
| **Jenkins Pipeline**     | ~50          | Per deployment      |
| **AWS Resources**        | ~100         | 60 seconds          |
| **Total**                | **~1,070**   | Various             |

### OpenTelemetry Collector Configuration

```yaml
receivers:
  hostmetrics:
    collection_interval: 10s
    scrapers: [cpu, disk, filesystem, memory, network, process]

  prometheus:
    config:
      scrape_configs:
        - job_name: "car-price-backend"
          static_configs:
            - targets: ["localhost:5002"]
          metrics_path: "/metrics/json"
          scrape_interval: 30s

        - job_name: "car-price-frontend"
          static_configs:
            - targets: ["localhost:3000"]
          metrics_path: "/metrics/json"
          scrape_interval: 30s

processors:
  resourcedetection:
    detectors: [env, ec2, system]

  attributes:
    actions:
      - key: service.name
        value: "car-price-predictor"
        action: upsert
      - key: environment
        value: "production"
        action: upsert

exporters:
  signalfx:
    access_token: "{{ splunk_token }}"
    realm: "{{ splunk_realm }}"
```

### Monitoring Metrics Available

#### **Backend Metrics**
- `car_price.system.cpu_percent` - System CPU usage
- `car_price.system.memory_percent` - Memory utilization
- `car_price.system.disk_usage` - Disk usage percentage
- `car_price.app.uptime_seconds` - Application uptime
- `car_price.app.total_requests` - Total API requests
- `car_price.app.total_predictions` - ML predictions made
- `car_price.business.avg_prediction_value` - Average car price predicted
- `car_price.business.model_accuracy` - ML model accuracy
- `car_price.business.active_users` - Active user count

#### **Frontend Metrics**
- `car_price.frontend.cpu_percent` - Frontend CPU usage
- `car_price.frontend.memory_percent` - Frontend memory usage
- `car_price.frontend.uptime_seconds` - Frontend uptime
- `car_price.frontend.total_requests` - Web requests
- `car_price.frontend.prediction_requests` - Prediction requests
- `car_price.frontend.publish_requests` - Vehicle publish requests
- `car_price.frontend.page_load_time` - Page load performance

#### **DevOps Pipeline Metrics**
- `jenkins.pipeline.success/failure` - Pipeline results
- `jenkins.terraform.apply.duration` - Infrastructure deployment time
- `jenkins.ansible.deploy.duration` - Configuration deployment time
- `terraform.ec2.deployment` - Infrastructure changes
- `ansible.deployment.success` - Configuration success

---

## 🔧 Jenkins Pipeline Implementation

### Jenkins Pipeline with Splunk Metrics

```groovy
pipeline {
    agent any

    environment {
        SPLUNK_TOKEN = 'PZuf3J0L2Op_Qj9hpAJzlw'
        SPLUNK_REALM = 'us1'
        SPLUNK_URL = "https://ingest.${SPLUNK_REALM}.signalfx.com/v2/datapoint"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                script {
                    sendSplunkMetric('jenkins.stage.checkout', 1, [
                        stage: 'checkout',
                        job: env.JOB_NAME,
                        build: env.BUILD_NUMBER
                    ])
                }
            }
        }

        stage('Terraform Plan') {
            steps {
                script {
                    def startTime = System.currentTimeMillis()

                    sh '''
                        cd terraform
                        terraform init
                        terraform plan -out=tfplan
                    '''

                    def duration = (System.currentTimeMillis() - startTime) / 1000
                    sendSplunkMetric('jenkins.terraform.plan.duration', duration, [
                        stage: 'terraform-plan',
                        job: env.JOB_NAME
                    ])
                }
            }
        }

        stage('Terraform Apply') {
            steps {
                script {
                    def startTime = System.currentTimeMillis()

                    sh '''
                        cd terraform
                        terraform apply -auto-approve tfplan
                    '''

                    def duration = (System.currentTimeMillis() - startTime) / 1000
                    sendSplunkMetric('jenkins.terraform.apply.duration', duration, [
                        stage: 'terraform-apply',
                        job: env.JOB_NAME
                    ])
                }
            }
        }

        stage('Ansible Deploy') {
            steps {
                script {
                    def startTime = System.currentTimeMillis()

                    sh '''
                        cd ansible
                        ansible-playbook -i inventory splunk-observability.yml
                        ansible-playbook -i inventory deploy-app.yml
                    '''

                    def duration = (System.currentTimeMillis() - startTime) / 1000
                    sendSplunkMetric('jenkins.ansible.deploy.duration', duration, [
                        stage: 'ansible-deploy',
                        job: env.JOB_NAME
                    ])
                }
            }
        }

        stage('Health Check') {
            steps {
                script {
                    def ec2Ip = sh(
                        script: 'cd terraform && terraform output -raw ec2_public_ip',
                        returnStdout: true
                    ).trim()

                    // Check backend health
                    def backendHealth = sh(
                        script: "curl -f http://${ec2Ip}:5002/health",
                        returnStatus: true
                    )

                    // Check frontend health
                    def frontendHealth = sh(
                        script: "curl -f http://${ec2Ip}:3000/health",
                        returnStatus: true
                    )

                    sendSplunkMetric('jenkins.health.backend', backendHealth == 0 ? 1 : 0, [
                        service: 'backend',
                        ec2_ip: ec2Ip
                    ])

                    sendSplunkMetric('jenkins.health.frontend', frontendHealth == 0 ? 1 : 0, [
                        service: 'frontend',
                        ec2_ip: ec2Ip
                    ])
                }
            }
        }
    }

    post {
        success {
            script {
                sendSplunkMetric('jenkins.pipeline.success', 1, [
                    job: env.JOB_NAME,
                    build: env.BUILD_NUMBER,
                    result: 'success'
                ])
            }
        }
        failure {
            script {
                sendSplunkMetric('jenkins.pipeline.failure', 1, [
                    job: env.JOB_NAME,
                    build: env.BUILD_NUMBER,
                    result: 'failure'
                ])
            }
        }
    }
}

def sendSplunkMetric(metricName, value, dimensions) {
    def payload = [
        gauge: [[
            metric: metricName,
            value: value,
            dimensions: dimensions + [
                timestamp: System.currentTimeMillis(),
                jenkins_url: env.JENKINS_URL,
                node_name: env.NODE_NAME
            ]
        ]]
    ]

    sh """
        curl -X POST ${SPLUNK_URL} \
        -H "X-SF-Token: ${SPLUNK_TOKEN}" \
        -H "Content-Type: application/json" \
        -d '${groovy.json.JsonBuilder(payload).toString()}'
    """
}
```

---

## 🎯 Alerting Framework

### Critical Alert Thresholds

```yaml
# Infrastructure Alerts
- CPU Usage > 85%
- Memory Usage > 90%
- Disk Usage > 95%
- Network Errors > 5%

# Application Alerts
- API Response Time > 2 seconds
- Error Rate > 5%
- Prediction Accuracy < 80%
- Service Downtime > 1 minute

# Pipeline Alerts
- Deployment Failure
- Terraform Apply Failure
- Ansible Configuration Failure
```

### Troubleshooting Framework

| Issue                 | Symptoms                   | Solution                               |
| --------------------- | -------------------------- | -------------------------------------- |
| **Missing Metrics**   | No data in Splunk          | Check OpenTelemetry Collector status   |
| **High CPU Usage**    | System slow, alerts firing | Scale EC2 instance or optimize app     |
| **Pipeline Failures** | Deployment errors          | Check Jenkins logs and Terraform state |
| **App Downtime**      | Health checks failing      | Restart services, check logs           |

---

## 📊 Available Dashboards

### **Backend Dashboard** (Port 5002/dashboard)
- **System Metrics**: CPU, Memory, Uptime
- **API Performance**: Total requests, ML predictions
- **Real-time Updates**: Auto-refresh every 5 seconds
- **Splunk Integration**: Direct link to observability platform

### **Frontend Dashboard** (Port 3000/dashboard)
- **Web Metrics**: User requests, predictions, publishes
- **System Performance**: CPU, Memory usage
- **User Activity**: Real-time interaction tracking
- **Health Status**: Service connectivity monitoring

### **Splunk Observability Cloud**
- **Comprehensive Metrics**: 1,070+ metrics/hour
- **Real-time Visualization**: Live data streaming
- **Historical Analysis**: 30-day data retention
- **Custom Dashboards**: Business and technical KPIs

---

## 🚀 Implemented Metrics

### **Backend Metrics (Actually Implemented)**

```python
# System Performance Metrics
car_price.system.cpu_percent        # Real-time CPU usage
car_price.system.memory_percent     # Real-time memory usage
car_price.system.disk_usage         # Disk usage percentage

# Application Metrics
car_price.app.uptime_seconds        # Application uptime
car_price.app.total_requests        # Total API requests
car_price.app.total_predictions     # ML predictions made

# Business KPIs (Simulated)
car_price.business.avg_prediction_value  # Average car price predicted
car_price.business.model_accuracy        # ML model accuracy (simulated)
car_price.business.active_users          # Active user count (simulated)

# Prediction Tracking
car_price.predictions.current_value      # Current price predictions
car_price.predictions.future_value       # Future price predictions
car_price.business.months_forecast       # Forecast months requested
car_price.requests.total                 # Total requests counter
```

### **Frontend Metrics (Actually Implemented)**

```python
# System Performance Metrics
car_price.frontend.cpu_percent           # Frontend CPU usage
car_price.frontend.memory_percent        # Frontend memory usage

# Application Metrics
car_price.frontend.uptime_seconds        # Frontend uptime
car_price.frontend.total_requests        # Total web requests
car_price.frontend.prediction_requests   # Prediction requests
car_price.frontend.publish_requests      # Vehicle publish requests

# User Experience Metrics
car_price.frontend.page_load_time        # Page load performance (simulated)
car_price.frontend.predictions           # User prediction actions
car_price.frontend.publishes             # User publish actions
car_price.frontend.requests.total        # Frontend request counter
car_price.frontend.publish.total         # Publish counter
```

### **Real-time Monitoring Features**

- **Continuous Metrics**: Both services send metrics every 10 seconds
- **Event-driven Metrics**: Metrics sent on user actions (predictions, publishes)
- **System Monitoring**: CPU, memory, disk usage tracking
- **Business Analytics**: Prediction values, model accuracy, user engagement
- **Health Checks**: Service status and connectivity monitoring
- **Dashboard Integration**: Real-time dashboards with auto-refresh



---

## 🔧 Deployment Commands

### **Infrastructure Deployment**
```bash
# 1. Deploy infrastructure
cd terraform
terraform init
terraform plan
terraform apply

# 2. Configure monitoring
cd ../ansible
ansible-playbook -i inventory splunk-observability.yml

# 3. Deploy application
ansible-playbook -i inventory deploy-app.yml

# 4. Verify monitoring
curl http://13.220.64.167:5002/health
curl http://13.220.64.167:3000/health
```

### **Access Points**
- **Splunk Observability**: https://app.us1.signalfx.com
- **Production Application**: http://13.220.64.167:3000/
- **Backend Dashboard**: http://13.220.64.167:5002/dashboard
- **Frontend Dashboard**: http://13.220.64.167:3000/dashboard
- **Health Checks**: http://13.220.64.167:5002/health & http://13.220.64.167:3000/health

---

## Implementation Summary

**Platform Status**: Production-ready ML prediction service with enterprise DevOps architecture
**Monitoring Coverage**: Application, infrastructure, and pipeline metrics with Splunk Observability Cloud
**Architecture**: 3-repository structure with Terraform IaC, Ansible configuration, and Flask application
**Deployment**: Jenkins CI/CD pipeline with automated AWS provisioning and monitoring integration
**Team**: Jose Rubio (Project Lead) | Full-stack MLOps | SCRUM methodology

---

---

*Enterprise DevOps documentation for Car Price Prediction Platform - Complete AWS deployment with comprehensive observability and monitoring.*
