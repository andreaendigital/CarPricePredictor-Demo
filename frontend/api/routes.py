from flask import jsonify, request
from . import api_bp
from logic.data_processor import get_current_value
from logic.predictor import get_predictions


@api_bp.route("/valoractual", methods=["POST"])
def valoractual():
    """
    Get current market value
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            model_year:
              type: integer
            age:
              type: integer
            fuel_type:
              type: string
            transmission:
              type: string
            clean_title:
              type: string
    responses:
      200:
        description: Current market value data
    """
    data = request.get_json()
    return jsonify(get_current_value(data))


@api_bp.route("/predictions", methods=["POST"])
def predictions():
    """
    Get car price predictions
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            model_year:
              type: integer
              example: 2020
            age:
              type: integer
              example: 4
            fuel_type:
              type: string
              example: "Gasoline"
            transmission:
              type: string
              example: "Automatic"
            clean_title:
              type: string
              example: "Yes"
    responses:
      200:
        description: Price prediction
    """
    data = request.get_json()
    return jsonify(get_predictions(data))
