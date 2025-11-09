# 🚀 AWS EC2 Observability Setup Guide
## Complete Splunk Observability Cloud Integration for CarPricePredictor

## 📋 **Overview**

This guide shows how to deploy the CarPricePredictor app to AWS EC2 with **full Splunk Observability Cloud integration** using Terraform, Ansible, and Jenkins.

## 🎯 **What We'll Monitor**

### **Application Layer** (Already Integrated)
- ✅ CarPricePredictor app performance (720+ metrics/hour)
- ✅ ML prediction analytics and business KPIs
- ✅ User experience and system resource metrics

### **Infrastructure Layer** (New)
- 🆕 EC2 instance health (CPU, memory, disk, network)
- 🆕 AWS CloudWatch integration
- 🆕 Load balancer performance
- 🆕 Auto Scaling Group metrics

### **DevOps Pipeline** (New)
- 🆕 Terraform deployment metrics
- 🆕 Ansible playbook execution times
- 🆕 Jenkins pipeline performance
- 🆕 Infrastructure drift detection

## 🛠️ **Implementation Steps**

### **Step 1: Terraform Configuration**

Create `terraform/monitoring.tf`:
```hcl
# Splunk Observability Cloud integration
variable "splunk_observability_token" {
  description = "Splunk Observability Cloud token"
  type        = string
  default     = "PZuf3J0L2Op_Qj9hpAJzlw"
  sensitive   = true
}

variable "splunk_realm" {
  description = "Splunk realm"
  type        = string
  default     = "us1"
}

# EC2 Instance with Splunk integration
resource "aws_instance" "car_price_app" {
  ami           = "ami-0c02fb55956c7d316"  # Amazon Linux 2
  instance_type = "t3.medium"
  key_name      = var.key_name

  vpc_security_group_ids = [aws_security_group.car_price_sg.id]
  subnet_id              = aws_subnet.public.id

  # Install Splunk OpenTelemetry Collector
  user_data = templatefile("${path.module}/scripts/install_splunk_agent.sh", {
    splunk_token = var.splunk_observability_token
    splunk_realm = var.splunk_realm
  })

  tags = {
    Name        = "CarPricePredictor-App"
    Environment = "production"
    Application = "car-price-predictor"
    Monitoring  = "splunk-observability"
    Service     = "ml-prediction-api"
  }
}

# Security Group
resource "aws_security_group" "car_price_sg" {
  name_description = "CarPricePredictor Security Group"
  vpc_id          = aws_vpc.main.id

  # Application ports
  ingress {
    from_port   = 3000
    to_port     = 3000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 5002
    to_port     = 5002
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # SSH access
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "CarPricePredictor-SG"
  }
}

# Application Load Balancer
resource "aws_lb" "car_price_alb" {
  name               = "car-price-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.car_price_sg.id]
  subnets           = [aws_subnet.public.id, aws_subnet.public_2.id]

  tags = {
    Name        = "CarPricePredictor-ALB"
    Environment = "production"
    Monitoring  = "splunk-observability"
  }
}

# Output EC2 public IP
output "ec2_public_ip" {
  value = aws_instance.car_price_app.public_ip
}

output "load_balancer_dns" {
  value = aws_lb.car_price_alb.dns_name
}
```

Create `terraform/scripts/install_splunk_agent.sh`:
```bash
#!/bin/bash
# Install Splunk OpenTelemetry Collector

# Update system
yum update -y
yum install -y curl wget

# Install Splunk OpenTelemetry Collector
curl -sSL https://dl.signalfx.com/splunk-otel-collector.sh > /tmp/splunk-otel-collector.sh
sudo sh /tmp/splunk-otel-collector.sh --realm ${splunk_realm} --token ${splunk_token}

# Configure collector for EC2 metadata
cat > /etc/otel/collector/agent_config.yaml << EOF
receivers:
  hostmetrics:
    collection_interval: 10s
    scrapers:
      cpu:
      disk:
      filesystem:
      memory:
      network:
      process:

processors:
  resourcedetection:
    detectors: [env, ec2, system]
    timeout: 5s

exporters:
  signalfx:
    access_token: ${splunk_token}
    realm: ${splunk_realm}

service:
  pipelines:
    metrics:
      receivers: [hostmetrics]
      processors: [resourcedetection]
      exporters: [signalfx]
EOF

# Restart collector
systemctl restart splunk-otel-collector
systemctl enable splunk-otel-collector

# Send deployment metric
curl -X POST https://ingest.${splunk_realm}.signalfx.com/v2/datapoint \
  -H "X-SF-Token: ${splunk_token}" \
  -H "Content-Type: application/json" \
  -d '{"gauge":[{"metric":"terraform.ec2.deployment","value":1,"dimensions":{"environment":"production","service":"car-price-app","deployment_method":"terraform"}}]}'
EOF
```

### **Step 2: Ansible Playbook Integration**

Create `ansible/splunk-observability.yml`:
```yaml
---
- name: Configure Splunk Observability Cloud Integration
  hosts: ec2_instances
  become: yes
  vars:
    splunk_token: "PZuf3J0L2Op_Qj9hpAJzlw"
    splunk_realm: "us1"

  tasks:
    - name: Verify Splunk OTel Collector is running
      systemd:
        name: splunk-otel-collector
        state: started
        enabled: yes

    - name: Install additional monitoring tools
      yum:
        name:
          - htop
          - iotop
          - nethogs
        state: present

    - name: Configure application-specific metrics
      template:
        src: app_metrics_config.yaml.j2
        dest: /etc/otel/collector/app_config.yaml
      notify: restart splunk collector

    - name: Send Ansible deployment metric
      uri:
        url: "https://ingest.{{ splunk_realm }}.signalfx.com/v2/datapoint"
        method: POST
        headers:
          X-SF-Token: "{{ splunk_token }}"
          Content-Type: "application/json"
        body_format: json
        body:
          gauge:
            - metric: "ansible.deployment.success"
              value: 1
              dimensions:
                environment: "production"
                service: "car-price-app"
                playbook: "splunk-observability"
                host: "{{ inventory_hostname }}"

  handlers:
    - name: restart splunk collector
      systemd:
        name: splunk-otel-collector
        state: restarted
```

Create `ansible/templates/app_metrics_config.yaml.j2`:
```yaml
# Application-specific metrics configuration
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'car-price-backend'
          static_configs:
            - targets: ['localhost:5002']
          metrics_path: '/metrics/json'
          scrape_interval: 30s

        - job_name: 'car-price-frontend'
          static_configs:
            - targets: ['localhost:3000']
          metrics_path: '/metrics/json'
          scrape_interval: 30s

processors:
  attributes:
    actions:
      - key: service.name
        value: "car-price-predictor"
        action: upsert
      - key: environment
        value: "production"
        action: upsert
      - key: deployment.method
        value: "ansible"
        action: upsert

exporters:
  signalfx:
    access_token: "{{ splunk_token }}"
    realm: "{{ splunk_realm }}"

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      processors: [attributes]
      exporters: [signalfx]
```

### **Step 3: Jenkins Pipeline Integration**

Create `Jenkinsfile` with Splunk metrics:
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

### **Step 4: Application Configuration**

The CarPricePredictor app already has Splunk Observability integration. Ensure these environment variables are set on EC2:

```bash
# /etc/environment
SPLUNK_TOKEN=PZuf3J0L2Op_Qj9hpAJzlw
SPLUNK_REALM=us1
ENVIRONMENT=production
SERVICE_NAME=car-price-predictor
```

## 📊 **Monitoring Dashboards**

### **Access Points**
- **Splunk Observability**: https://app.us1.signalfx.com
- **Backend Dashboard**: `http://your-ec2-ip:5002/dashboard`
- **Frontend Dashboard**: `http://your-ec2-ip:3000/dashboard`
- **Health Checks**: `http://your-ec2-ip:5002/health` & `http://your-ec2-ip:3000/health`

### **Key Metrics Available**

#### **Infrastructure Metrics**
- `aws.ec2.cpu_utilization` - EC2 CPU usage
- `aws.ec2.memory_utilization` - EC2 memory usage
- `aws.ec2.disk_utilization` - EC2 disk usage
- `aws.ec2.network_in/out` - Network traffic
- `aws.applicationelb.request_count` - Load balancer requests

#### **Application Metrics** (Already Integrated)
- `car_price.system.cpu_percent` - App CPU usage
- `car_price.app.total_requests` - API requests
- `car_price.business.avg_prediction_value` - ML predictions
- `car_price.frontend.user_satisfaction` - User experience

#### **DevOps Pipeline Metrics**
- `jenkins.pipeline.success/failure` - Pipeline results
- `jenkins.terraform.apply.duration` - Infrastructure deployment time
- `jenkins.ansible.deploy.duration` - Configuration deployment time
- `terraform.ec2.deployment` - Infrastructure changes
- `ansible.deployment.success` - Configuration success

## 🚀 **Deployment Commands**

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
curl http://$(terraform output -raw ec2_public_ip):5002/health
curl http://$(terraform output -raw ec2_public_ip):3000/health
```

## ✅ **Expected Results**

### **Immediate Benefits**
- **Complete Infrastructure Visibility** - EC2, Load Balancer, Network metrics
- **Application Performance Monitoring** - 720+ metrics/hour from CarPricePredictor
- **DevOps Pipeline Analytics** - Jenkins, Terraform, Ansible metrics
- **Real-time Alerting** - Proactive issue detection
- **Single Pane of Glass** - All metrics in Splunk Observability Cloud

### **Metrics Volume**
- **Infrastructure**: ~200 metrics/hour per EC2 instance
- **Application**: ~720 metrics/hour (backend + frontend)
- **DevOps Pipeline**: ~50 metrics per deployment
- **Total**: ~1,000+ metrics/hour comprehensive observability

## 🎯 **Success Criteria**

✅ **Infrastructure deployed** via Terraform with Splunk integration
✅ **Application configured** via Ansible with monitoring enabled
✅ **Pipeline metrics** flowing from Jenkins to Splunk Observability
✅ **Health checks** passing for all services
✅ **Dashboards accessible** with real-time data
✅ **Alerts configured** for critical thresholds

**Result**: Complete end-to-end observability from code to cloud infrastructure.
