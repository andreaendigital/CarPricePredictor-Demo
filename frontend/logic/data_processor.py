def get_current_value(car_data=None):
    """Fetch current market value based on car details"""
    if car_data is None:
        return {"error": "No car data provided"}

    # Calculate market value based on car features
    base_value = 12000
    year_factor = (car_data.get("model_year", 2020) - 2000) * 300
    age_penalty = car_data.get("age", 0) * 800

    # Fuel type adjustments
    fuel_bonus = {"Electric": 3000, "Hybrid": 1500, "Gasoline": 0, "Diesel": -500}.get(
        car_data.get("fuel_type", "Gasoline"), 0
    )

    current_value = base_value + year_factor - age_penalty + fuel_bonus

    return {
        "current_market_value": max(current_value, 5000),
        "car_details": car_data,
        "timestamp": "2024-01-01T12:00:00Z",
    }
