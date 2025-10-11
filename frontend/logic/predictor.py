def get_predictions(car_data=None):
    """Generate car price predictions using ML model"""
    if car_data is None:
        return {"error": "No car data provided"}

    # Required features: model_year, age, fuel_type, transmission, clean_title
    required_features = [
        "model_year",
        "age",
        "fuel_type",
        "transmission",
        "clean_title",
    ]

    # Validate input
    for feature in required_features:
        if feature not in car_data:
            return {"error": f"Missing required feature: {feature}"}

    # TODO: Load actual trained model and make prediction
    # For now, return demo prediction based on input
    predicted_price = 15000 + (car_data["model_year"] - 2000) * 500 - car_data["age"] * 1000

    return {
        "predicted_price": predicted_price,
        "input_features": car_data,
        "model": "used_cars_model",
    }
