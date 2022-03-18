from flask import Blueprint
from flask_pydantic import validate

from src.services.service import get_model_output
from src.models.models import ModelOutputRequest

model_blueprint = Blueprint('model', __name__)


@model_blueprint.route("/sentiment-analysis", methods=["POST"])
@validate()
def get_sentiment(body: ModelOutputRequest):
    try:
        if body.model.isalpha():
            return get_model_output(body)
    except ValueError as ev:
        return "Invalid input"


