# 🚗 Car Price Prediction Platform - Enterprise MLOps Solution

## 📋 Project Overview

**Professional full-stack machine learning platform** for automotive price prediction and vehicle marketplace management. Built with enterprise-grade architecture, comprehensive API documentation, and modern web technologies.

### 🎯 Business Value
- **Real-time ML Predictions** - Instant vehicle valuations using XGBoost algorithms
- **Future Price Forecasting** - AI-powered depreciation modeling for investment decisions  
- **Marketplace Integration** - Complete vehicle listing and price recommendation system
- **Professional Documentation** - Multiple API documentation formats for different stakeholders

## 🏗️ Architecture Overview

```
📁 Car Price Prediction Platform
├── 🎨 frontend/          # Modern Web Interface (Port 3000)
│   ├── 🖥️  templates/     # Professional HTML5 templates
│   ├── 🎨 static/        # CSS3 animations & JavaScript
│   ├── 🔧 api/           # Flask blueprints & routing
│   ├── ⚙️  config/       # Application configuration
│   ├── 🧠 logic/         # Business logic layer
│   └── 🧪 tests/         # Unit & integration tests
│
├── 🚀 backend/           # ML API Services (Port 5002/5004)
│   ├── 🤖 modelo/        # Trained XGBoost ML model
│   ├── 📊 app.py         # Lightweight ML API
│   ├── 📚 app_swagger.py # Enterprise Swagger API
│   └── 📖 Documentation  # Professional API docs
│
└── 📋 Documentation      # Project documentation
```

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.9+
- Flask ecosystem
- XGBoost ML framework
- Modern web browser

### 🔧 Backend Setup (ML API)
```bash
cd backend
pip install -r requirements.txt
python3 app.py              # Simple API (Port 5002) - Frontend connects here
# OR
python3 app_swagger.py      # Professional Swagger API (Port 5004) - Documentation only
```

### 🎨 Frontend Setup (Web Interface)
```bash
cd frontend
pip install flask
python3 app.py              # Web interface (Port 3000)
```

### 🔗 Frontend-Backend Connection
- **Frontend** (Port 3000) connects to **Backend** (Port 5002)
- Start backend first, then frontend for proper API connectivity
- CORS enabled for cross-origin requests between services

### 🌐 Access Points
- **Web Application**: `http://localhost:3000` (Main Interface)
- **Backend API**: `http://localhost:5002` (ML Predictions)
- **API Documentation**: `http://localhost:5004/docs-menu` (Swagger Only)
- **Swagger UI**: `http://localhost:5004/docs/`
- **ReDoc**: `http://localhost:5004/redoc`

## 📊 API Endpoints

### 🔍 Price Prediction Services
| Endpoint | Method | Description | Parameters |
|----------|--------|-------------|------------|
| `/precio_actual` | GET | Current market valuation | model_year, age, fuel_type, transmission, clean_title |
| `/prediccion_futura` | GET | Future price forecasting | Same as above + meses (months) |
| `/publicar_vehiculo` | POST | Vehicle marketplace listing | Vehicle data + precio (listing price) |

### 📈 Sample API Calls
```bash
# Current Price Prediction
curl "http://localhost:5002/precio_actual?model_year=2020&age=4&fuel_type=Gasoline&transmission=Automatic&clean_title=1"

# Future Price Forecasting (12 months)
curl "http://localhost:5002/prediccion_futura?model_year=2020&age=4&fuel_type=Gasoline&transmission=Automatic&clean_title=1&meses=12"

# Vehicle Publishing
curl -X POST http://localhost:5002/publicar_vehiculo \
  -H "Content-Type: application/json" \
  -d '{"model_year": 2020, "age": 4, "fuel_type": "Gasoline", "transmission": "Automatic", "clean_title": 1, "precio": 25000000}'
```

## 🛠️ Technical Stack

### Backend Technologies
- **Framework**: Flask + Flask-RESTX
- **ML Engine**: XGBoost (Gradient Boosting)
- **API Documentation**: Swagger/OpenAPI 3.0
- **Data Storage**: JSON-based persistence
- **CORS**: Cross-origin resource sharing enabled

### Frontend Technologies
- **Framework**: Flask + Jinja2 templating
- **Styling**: CSS3 with animations and gradients
- **JavaScript**: ES6+ with Fetch API
- **UI/UX**: Responsive design with professional styling
- **Testing**: Unit and integration test suites

### Documentation Formats
- **Swagger UI** - Interactive API testing
- **ReDoc** - Professional dark theme documentation
- **RapiDoc** - Modern interactive documentation
- **Stoplight Elements** - Enterprise-grade documentation
- **Scalar** - Elegant modern API documentation

## 🎨 Professional Features

### 🖥️ Frontend Capabilities
- **Responsive Design** - Mobile-first approach
- **Professional Animations** - CSS3 transitions and effects
- **Real-time Validation** - Form validation and error handling
- **Modern UI Components** - Cards, gradients, and professional typography
- **Cross-browser Compatibility** - Tested across major browsers

### 🚀 Backend Capabilities
- **ML Model Integration** - Production-ready XGBoost model
- **Professional API Design** - RESTful architecture with proper HTTP status codes
- **Comprehensive Documentation** - Multiple documentation formats
- **Error Handling** - Robust error handling and validation
- **CORS Support** - Cross-origin requests enabled

## 📈 Machine Learning Model

### Model Specifications
- **Algorithm**: XGBoost (Extreme Gradient Boosting)
- **Features**: model_year, age, fuel_type, transmission, clean_title
- **Output**: Price prediction in local currency
- **Accuracy**: Production-ready model with depreciation modeling

### Prediction Types
1. **Current Market Value** - Real-time price estimation
2. **Future Price Forecasting** - Depreciation-based future value prediction
3. **Price Recommendations** - Marketplace listing price suggestions

## 🔧 Development Workflow

### Branch Strategy (SCRUM Methodology)
- **SCRUM-57**: Frontend development and UI/UX
- **SCRUM-58**: Backend API development
- **SCRUM-74**: Documentation and project setup
- **SCRUM-88**: Advanced backend with Swagger integration
- **SCRUM-89**: Unified full-stack solution (Current)

### Quality Assurance
- **Unit Testing** - Comprehensive test coverage
- **Integration Testing** - End-to-end workflow testing
- **Code Quality** - Professional coding standards
- **Documentation** - Extensive technical documentation

## 🧪 Testing Strategy

### Test Suite Overview
Our comprehensive testing strategy ensures code quality and reliability across all components:

#### **Backend Tests**
- **Location**: `tests/test_backend.py`
- **Coverage**: ML API endpoints, model predictions, error handling
- **Framework**: pytest with coverage reporting
- **Command**: `cd backend && python -m pytest ../tests/test_backend.py -v --cov=.`

#### **Frontend Tests**
- **API Endpoint Tests**: `frontend/tests/test_api_endpoints.py`
  - Tests POST `/valoractual` and `/predictions` endpoints
  - Validates JSON response structure and data types
  - Ensures proper error handling
- **Logic Unit Tests**: `frontend/tests/test_logic_unit.py`
  - Tests business logic functions in isolation
  - Validates price calculation algorithms
  - Tests data processing functions
- **Command**: `cd frontend && python -m pytest tests/ -v --cov=.`

#### **Integration Tests**
- **Location**: `tests/test_integration.py`
- **Purpose**: End-to-end testing with real services
- **Coverage**: 
  - Backend service health checks (Port 5002)
  - Frontend service health checks (Port 3000)
  - Complete prediction workflow testing
  - CORS functionality validation
- **Dependencies**: Requires `requests` library
- **Command**: `python -m pytest tests/test_integration.py -v`

### Code Quality Tools
- **Black**: Python code formatting (`black --check backend/ frontend/`)
- **Flake8**: Linting and style checking
- **pytest-cov**: Test coverage reporting
- **Coverage Reports**: XML format for CI/CD integration

## 🚀 CI/CD Pipeline

### GitHub Actions Workflow
Our automated pipeline ensures code quality and enables continuous deployment:

#### **Pipeline Stages**

**1. 🧪 Test & Quality Stage**
- **Triggers**: Push to `main`, `develop`, `feature/*`, `SCRUM-*` branches
- **Matrix Testing**: Python 3.9 and 3.11
- **Dependencies**: 
  ```bash
  pip install flake8 pytest pytest-cov black requests
  pip install -r backend/requirements.txt
  pip install -r frontend/requirements.txt
  ```
- **Quality Checks**:
  - Code formatting validation with Black
  - Linting with Flake8 (complexity max 10, line length 127)
  - Backend unit tests with coverage
  - Frontend unit tests with coverage
  - Integration tests with service health checks

**2. 🐳 Build Images Stage** *(Currently Disabled)*
- **Purpose**: Docker containerization for deployment
- **Images**: Backend and Frontend containers
- **Registry**: GitHub Container Registry (ghcr.io)
- **Status**: Temporarily disabled due to organization permissions

**3. 🚀 Deploy to Development**
- **Triggers**: `develop` branch or `SCRUM-*` branches
- **Environment**: Development staging
- **Purpose**: Testing new features before production
- **Dependencies**: Requires successful test and build stages

**4. 🌟 Deploy to Production**
- **Triggers**: Only `main` branch
- **Environment**: Production
- **Purpose**: Live application deployment
- **Requirements**: All tests must pass, manual approval required

#### **Pipeline Configuration**
```yaml
name: 🚗 Car Price Prediction CI/CD
triggers: [main, develop, feature/*, SCRUM-*]
matrix: [Python 3.9, Python 3.11]
stages: [Test & Quality → Build → Deploy]
```

#### **Test Execution Flow**
1. **Setup Environment**: Install Python dependencies
2. **Code Quality**: Black formatting + Flake8 linting
3. **Backend Testing**: ML API and model validation
4. **Frontend Testing**: UI components and API integration
5. **Integration Testing**: End-to-end workflow validation
6. **Coverage Reporting**: Generate XML coverage reports
7. **Deployment**: Automatic deployment based on branch

### Branch-Based Deployment Strategy
- **SCRUM-90** (Current) → Development Environment
- **develop** → Development Environment  
- **main** → Production Environment
- **feature/** → Development Environment (on push)

### Quality Gates
- ✅ All tests must pass (Backend, Frontend, Integration)
- ✅ Code formatting must comply with Black standards
- ✅ Linting must pass Flake8 checks
- ✅ Test coverage reports generated
- ✅ No critical security vulnerabilities

## 🚀 Deployment

### Development Environment (Recommended)
```bash
# Terminal 1: Start Backend API (Required for Frontend)
cd backend && python3 app.py

# Terminal 2: Start Frontend Web Interface
cd frontend && python3 app.py
```

### Alternative: Documentation Mode
```bash
# Terminal 1: Start Swagger Documentation Server
cd backend && python3 app_swagger.py

# Terminal 2: Start Frontend (will need port 5002 backend for API calls)
cd frontend && python3 app.py
```

### Production Considerations
- **Containerization**: Docker-ready architecture
- **Scalability**: Microservices-ready design
- **Security**: CORS configuration and input validation
- **Monitoring**: Comprehensive logging and error tracking

## 📋 Project Achievements

### ✅ Completed Features
- [x] Professional full-stack architecture
- [x] ML model integration with XGBoost
- [x] Multiple API documentation formats
- [x] Responsive web interface
- [x] Real-time price predictions
- [x] Future price forecasting
- [x] Vehicle marketplace functionality
- [x] Professional UI/UX design
- [x] Comprehensive testing suite (Unit + Integration + E2E)
- [x] CORS-enabled API architecture
- [x] Automated CI/CD pipeline with GitHub Actions
- [x] Multi-environment deployment (Dev/Prod)
- [x] Code quality automation (Black, Flake8, Coverage)
- [x] Branch-based deployment strategy

### 🎯 Business Impact
- **Reduced Development Time** - Unified architecture eliminates branch switching
- **Professional Presentation** - Multiple documentation formats for stakeholders
- **Scalable Solution** - Microservices-ready architecture
- **Enterprise-Ready** - Production-grade code quality and documentation

## 👥 Development Team

**Project Lead**: Jose Rubio  
**Architecture**: Full-stack MLOps solution  
**Methodology**: SCRUM/Agile development  
**Quality**: Enterprise-grade standards  

---

## 🎉 Getting Started

### Quick Start Options

#### Option 1: Local Services (Recommended)
```bash
# Start all services locally
bash start-local.sh
```

#### Option 2: Docker Environment
```bash
# Start with Docker containers
make run-dev

# Run tests
make test
```

### Manual Setup (Alternative)
1. **Clone Repository**: `git clone [repository-url]`
2. **Start Backend API**: `cd backend && python3 app.py` (Port 5002)
3. **Start Frontend**: `cd frontend && python3 app.py` (Port 3000)
4. **Access Application**: Visit `http://localhost:3000`

### 🌐 Access Points
- **Web Application**: `http://localhost:3000`
- **Backend API**: `http://localhost:5002`
- **API Documentation**: `http://localhost:5004`

**🚀 Ready for production deployment and enterprise integration!**