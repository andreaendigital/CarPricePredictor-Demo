# 🚗 Car Price Prediction API - Professional Documentation

## 📋 Documentation Hub - Main Access Point

**🎯 Primary Entry Point:** [Documentation Menu](http://localhost:5004/docs-menu)

Access our comprehensive API documentation through multiple professional interfaces:

| Documentation Type | URL | Description |
|-------------------|-----|-------------|
| **📋 Documentation Hub** | `/docs-menu` | **Main menu with all documentation options** |
| **🔧 Swagger UI** | `/docs/` | Interactive API testing interface |
| **🎨 ReDoc** | `/redoc` | Professional dark theme documentation |
| **⚡ RapiDoc** | `/rapidoc` | Modern interactive documentation |
| **💼 Elements** | `/elements` | Enterprise-grade Stoplight documentation |
| **✨ Scalar** | `/scalar` | Elegant modern API documentation |

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run API Server
```bash
python app_swagger.py
```

### 3. Access Documentation
```
http://localhost:5004/docs-menu
```

## 📊 API Endpoints Overview

### 🔍 Current Price Prediction
**GET** `/api/prediction/precio_actual`
- Predicts current market value
- Parameters: model_year, age, fuel_type, transmission, clean_title

### 📈 Future Price Forecasting
**GET** `/api/prediction/prediccion_futura`
- Forecasts price after specified months
- Additional parameter: meses (months ahead)

### 📝 Vehicle Listing Management
**POST** `/api/vehicles/publicar_vehiculo`
- Adds vehicle to marketplace
- Returns price recommendation vs listed price

## 🛠 Technical Stack

- **Framework:** Flask + Flask-RESTX
- **ML Model:** XGBoost (modelo/modelo.joblib)
- **Documentation:** Multiple professional formats
- **Data Storage:** JSON file (vehiculos.json)

## 📁 Project Structure
```
├── app_swagger.py          # Main Flask API with Swagger
├── requirements.txt        # Dependencies
├── readme_swagger.md       # This documentation
├── modelo/
│   └── modelo.joblib      # Trained ML model
└── vehiculos.json         # Vehicle data storage
```

## 🎨 Documentation Features

### Professional Styling
- **Dark Theme Support** (ReDoc, RapiDoc)
- **Interactive Testing** (Swagger UI, RapiDoc)
- **Enterprise Design** (Elements, Scalar)
- **Responsive Layout** (All formats)

### Advanced Features
- **Try It Out** functionality
- **Code examples** in multiple languages
- **Professional typography**
- **Comprehensive API schemas**

## 🔧 Development

### Environment Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Debug Mode
```bash
export FLASK_ENV=development
python app_swagger.py
```

## 📱 Usage Examples

### Current Price Prediction
```bash
curl "http://localhost:5004/api/prediction/precio_actual?model_year=2020&age=4&fuel_type=Gasoline&transmission=Automatic&clean_title=1"
```

### Future Price Forecasting
```bash
curl "http://localhost:5004/api/prediction/prediccion_futura?model_year=2020&age=4&fuel_type=Gasoline&transmission=Automatic&clean_title=1&meses=12"
```

### Vehicle Listing
```bash
curl -X POST http://localhost:5004/api/vehicles/publicar_vehiculo \
  -H "Content-Type: application/json" \
  -d '{"model_year": 2020, "age": 4, "fuel_type": "Gasoline", "transmission": "Automatic", "clean_title": 1, "precio": 25000000}'
```

---

**🎯 Start Here:** Visit [Documentation Menu](http://localhost:5004/docs-menu) to explore all available documentation formats and choose your preferred interface.
