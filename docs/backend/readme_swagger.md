# 🚗 Car Price Prediction API - Professional Documentation

## 📋 API Documentation

Access our API documentation through two streamlined interfaces:

| Documentation Type | URL | Description |
|-------------------|-----|-------------|
| **🔧 Swagger UI** | `/docs/` | Interactive API testing interface |
| **🎨 ReDoc** | `/redoc` | Professional documentation with dark theme |

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
Swagger UI: http://localhost:5004/docs/
ReDoc:      http://localhost:5004/redoc
```

## 📊 API Endpoints Overview

### 🔍 Current Price Prediction
**GET** `/api/prediction/current_value_market`
- Predicts current market value
- Parameters: model_year, age, fuel_type, transmission, clean_title

### 📈 Future Price Forecasting
**GET** `/api/prediction/future_prediction`
- Forecasts price after specified months
- Additional parameter: meses (months ahead)

### 📝 Vehicle Listing Management
**POST** `/api/vehicles/publish_car`
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
- **Dark Theme Support** (ReDoc)
- **Interactive Testing** (Swagger UI)
- **Responsive Layout** (Both formats)

### Advanced Features
- **Try It Out** functionality (Swagger UI)
- **Professional typography** (ReDoc)
- **Comprehensive API schemas** (Both formats)

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
curl "http://localhost:5004/api/prediction/current_value_market?model_year=2020&age=4&fuel_type=Gasoline&transmission=Automatic&clean_title=1"
```

### Future Price Forecasting
```bash
curl "http://localhost:5004/api/prediction/future_prediction?model_year=2020&age=4&fuel_type=Gasoline&transmission=Automatic&clean_title=1&meses=12"
```

### Vehicle Listing
```bash
curl -X POST http://localhost:5004/api/vehicles/publish_car \
  -H "Content-Type: application/json" \
  -d '{"model_year": 2020, "age": 4, "fuel_type": "Gasoline", "transmission": "Automatic", "clean_title": 1, "precio": 25000000}'
```

---

**🎯 Access Points:**
- **Interactive Testing:** [Swagger UI](http://localhost:5004/docs/)
- **Professional Docs:** [ReDoc](http://localhost:5004/redoc)
