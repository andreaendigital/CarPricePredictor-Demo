class CarPriceAPI {
  static CONFIG = {
    USE_FAKE_DATA: false, // Connected to real Swagger API
    PRODUCTION_URL: "https://your-production-server.com",
    ENDPOINTS: {
      CURRENT_PRICE: "/precio_actual",
      FUTURE_PRICE: "/prediccion_futura",
      PUBLISH_VEHICLE: "/publicar_vehiculo",
    },
  };

  static get BASE_URL() {
    // Check if running in Docker (frontend container)
    if (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1") {
      return "http://localhost:5002";
    }
    return CarPriceAPI.CONFIG.PRODUCTION_URL;
  }

  static ENDPOINTS = {
    CURRENT_PRICE: `${CarPriceAPI.BASE_URL}${CarPriceAPI.CONFIG.ENDPOINTS.CURRENT_PRICE}`,
    FUTURE_PRICE: `${CarPriceAPI.BASE_URL}${CarPriceAPI.CONFIG.ENDPOINTS.FUTURE_PRICE}`,
    PUBLISH_VEHICLE: `${CarPriceAPI.BASE_URL}${CarPriceAPI.CONFIG.ENDPOINTS.PUBLISH_VEHICLE}`,
  };

  static generateFakeCurrentValue(carData) {
    const baseValue =
      12000 + (carData.model_year - 2000) * 500 - carData.age * 800;
    const fuelBonus =
      { Electric: 3000, Hybrid: 1500, Gasoline: 0, Diesel: -500 }[
        carData.fuel_type
      ] || 0;
    return {
      current_market_value: Math.max(baseValue + fuelBonus, 5000),
      timestamp: new Date().toISOString(),
      car_details: carData,
    };
  }

  static generateFakePrediction(carData) {
    const predictedPrice =
      15000 + (carData.model_year - 2000) * 600 - carData.age * 900;
    return {
      predicted_price: Math.max(predictedPrice, 8000),
      input_features: carData,
      model: "demo_ml_model",
    };
  }

  static ELEMENTS = {
    CURRENT_VALUE: "currentValue",
    PREDICTIONS: "predictions",
  };

  static getFormData() {
    const fields = [
      "model_year",
      "age",
      "fuel_type",
      "transmission",
      "clean_title",
    ];
    return fields.reduce((data, field) => {
      const element = document.getElementById(field);
      data[field] = ["model_year", "age", "clean_title"].includes(field)
        ? parseInt(element.value)
        : element.value;
      return data;
    }, {});
  }

  static async makeRequest(endpoint, data, method = "GET") {
    if (CarPriceAPI.CONFIG.USE_FAKE_DATA) {
      // Simulate API delay
      await new Promise((resolve) => setTimeout(resolve, 500));

      if (endpoint.includes("/current-price")) {
        return CarPriceAPI.generateFakeCurrentValue(data);
      } else if (endpoint.includes("/future-price")) {
        return CarPriceAPI.generateFakePrediction(data);
      }
    }

    let url = endpoint;
    let options = {
      method: method,
      headers: { "Content-Type": "application/json" },
    };

    if (method === "GET") {
      // Build query string for GET requests
      const params = new URLSearchParams(data);
      url = `${endpoint}?${params}`;
    } else {
      // JSON body for POST requests
      options.body = JSON.stringify(data);
    }

    const response = await fetch(url, options);

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    return response.json();
  }

  static updateElement(elementId, content) {
    const element = document.getElementById(elementId);
    if (element) element.innerHTML = content;
  }

  static formatCurrency(amount) {
    return new Intl.NumberFormat("en-US", {
      style: "currency",
      currency: "USD",
      minimumFractionDigits: 0,
    }).format(amount);
  }

  static renderCurrentValue(data) {
    const featureMap = {
      model_year: { icon: '📆', label: 'Year' },
      age: { icon: '⏳', label: 'Age' },
      fuel_type: { icon: '⛽', label: 'Fuel' },
      transmission: { icon: '⚙️', label: 'Transmission' },
      clean_title: { icon: '📋', label: 'Title' }
    };

    const vehicleSpecs = Object.entries(data.datos)
      .map(([k, v]) => {
        const spec = featureMap[k] || { icon: '•', label: k };
        return `
          <div style="display: flex; align-items: center; justify-content: space-between; padding: 4px 10px; margin: 1px 0; background: linear-gradient(135deg, #f8f9fa, #e9ecef); border-radius: 6px; border-left: 3px solid #667eea;">
            <span style="font-size: 12px; color: #495057;"><strong>${spec.icon} ${spec.label}</strong></span>
            <span style="font-size: 16px; font-weight: 400; font-style: italic; color: #667eea; font-family: 'Georgia', serif;">${v}</span>
          </div>
        `;
      })
      .join('');

    return `
            <div class="fade-in" style="background: linear-gradient(135deg, #ffffff, #f8f9fa); border-radius: 12px; padding: 15px; border: 1px solid #e9ecef; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <div style="text-align: center; margin-bottom: 10px; padding-bottom: 8px; border-bottom: 2px solid #e9ecef;">
                    <div style="font-size: 14px; color: #6c757d; margin-bottom: 2px;">💲 Current Value</div>
                    <div style="font-size: 28px; font-weight: 700; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">${this.formatCurrency(data.precio_actual_estimado)}</div>
                </div>
                <div style="margin-bottom: 8px;">
                    <div style="font-size: 13px; font-weight: 600; color: #495057; margin-bottom: 6px; text-align: center;">Vehicle Analysis</div>
                    ${vehicleSpecs}
                </div>
                <div style="text-align: center; padding-top: 6px; border-top: 1px solid #e9ecef;">
                    <span style="font-size: 11px; color: #6c757d; background: #f8f9fa; padding: 3px 6px; border-radius: 10px;">🤖 ML Prediction</span>
                </div>
            </div>
        `;
  }

  static renderPrediction(data) {
    const featureMap = {
      model_year: { icon: '📆', label: 'Year' },
      age: { icon: '⏳', label: 'Age' },
      fuel_type: { icon: '⛽', label: 'Fuel' },
      transmission: { icon: '⚙️', label: 'Transmission' },
      clean_title: { icon: '📋', label: 'Title' }
    };

    const vehicleSpecs = Object.entries(data.datos)
      .map(([k, v]) => {
        const spec = featureMap[k] || { icon: '•', label: k };
        return `
          <div style="display: flex; align-items: center; justify-content: space-between; padding: 4px 10px; margin: 1px 0; background: linear-gradient(135deg, #f8f9fa, #e9ecef); border-radius: 6px; border-left: 3px solid #667eea;">
            <span style="font-size: 12px; color: #495057;"><strong>${spec.icon} ${spec.label}</strong></span>
            <span style="font-size: 16px; font-weight: 400; font-style: italic; color: #667eea; font-family: 'Georgia', serif;">${v}</span>
          </div>
        `;
      })
      .join('');

    return `
            <div class="fade-in" style="background: linear-gradient(135deg, #ffffff, #f8f9fa); border-radius: 12px; padding: 15px; border: 1px solid #e9ecef; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <div style="text-align: center; margin-bottom: 10px; padding-bottom: 8px; border-bottom: 2px solid #e9ecef;">
                    <div style="font-size: 14px; color: #6c757d; margin-bottom: 2px;">🔮 Future Prediction (${data.meses} months)</div>
                    <div style="font-size: 28px; font-weight: 700; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">${this.formatCurrency(data.precio_estimado_futuro)}</div>
                    <div style="font-size: 16px; color: #6c757d; margin-top: 4px;">Current: ${this.formatCurrency(data.precio_actual_estimado)}</div>
                </div>
                <div style="margin-bottom: 8px;">
                    <div style="font-size: 13px; font-weight: 600; color: #495057; margin-bottom: 6px; text-align: center;">Vehicle Analysis</div>
                    ${vehicleSpecs}
                </div>
                <div style="text-align: center; padding-top: 6px; border-top: 1px solid #e9ecef;">
                    <span style="font-size: 11px; color: #6c757d; background: #f8f9fa; padding: 3px 6px; border-radius: 10px;">📈 Depreciation Model</span>
                </div>
            </div>
        `;
  }

  static handleError(elementId, error) {
    console.error("API Error:", error);
    this.updateElement(elementId, `<strong>Error:</strong> ${error.message}`);
  }
}

async function getCurrentValue() {
  try {
    const carData = CarPriceAPI.getFormData();
    // Keep clean_title as number for backend API
    const response = await CarPriceAPI.makeRequest(
      CarPriceAPI.ENDPOINTS.CURRENT_PRICE,
      carData,
      "GET"
    );

    const content = response.error
      ? `<strong>Error:</strong> ${response.error}`
      : CarPriceAPI.renderCurrentValue(response);

    CarPriceAPI.updateElement(CarPriceAPI.ELEMENTS.CURRENT_VALUE, content);
  } catch (error) {
    CarPriceAPI.handleError(CarPriceAPI.ELEMENTS.CURRENT_VALUE, error);
  }
}

async function getPredictions() {
  try {
    const carData = CarPriceAPI.getFormData();
    // Keep clean_title as number for backend API
    // Add default months for future prediction
    carData.meses = 12;

    const response = await CarPriceAPI.makeRequest(
      CarPriceAPI.ENDPOINTS.FUTURE_PRICE,
      carData,
      "GET"
    );

    const content = response.error
      ? `<strong>Error:</strong> ${response.error}`
      : CarPriceAPI.renderPrediction(response);

    CarPriceAPI.updateElement(CarPriceAPI.ELEMENTS.PREDICTIONS, content);
  } catch (error) {
    CarPriceAPI.handleError(CarPriceAPI.ELEMENTS.PREDICTIONS, error);
  }
}

// New function for vehicle publishing
async function publishVehicle() {
  try {
    const carData = CarPriceAPI.getFormData();
    // Keep clean_title as number for backend API
    // Add a sample price for publishing
    carData.precio = 25000000;

    const response = await CarPriceAPI.makeRequest(
      CarPriceAPI.ENDPOINTS.PUBLISH_VEHICLE,
      carData,
      "POST"
    );

    const content = response.error
      ? `<strong>Error:</strong> ${response.error}`
      : `
        <div class="fade-in" style="background: linear-gradient(135deg, #d4edda, #c3e6cb); border-radius: 12px; padding: 15px; border: 1px solid #c3e6cb;">
          <div style="text-align: center; margin-bottom: 10px;">
            <div style="font-size: 18px; color: #155724; font-weight: 600;">✅ Vehicle Published Successfully!</div>
            <div style="font-size: 14px; color: #155724; margin-top: 5px;">ID: ${response.vehiculo_id}</div>
          </div>
          <div style="display: flex; justify-content: space-between; margin: 10px 0;">
            <div style="text-align: center;">
              <div style="font-size: 12px; color: #155724;">Your Price</div>
              <div style="font-size: 20px; font-weight: 600; color: #155724;">${CarPriceAPI.formatCurrency(response.precio_publicado)}</div>
            </div>
            <div style="text-align: center;">
              <div style="font-size: 12px; color: #155724;">Recommended</div>
              <div style="font-size: 20px; font-weight: 600; color: #155724;">${CarPriceAPI.formatCurrency(response.precio_recomendado_modelo)}</div>
            </div>
          </div>
        </div>
      `;

    CarPriceAPI.updateElement('publishResult', content);
  } catch (error) {
    CarPriceAPI.handleError('publishResult', error);
  }
}
