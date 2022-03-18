from flask import Blueprint
from flask_pydantic import validate

from src.services.service import check_sentiment_type_and_get_score
from src.models.models import ModelOutputRequest

model_blueprint = Blueprint('model', __name__)


@model_blueprint.route("/sentiment-analysis", methods=["POST"])
@validate()
def get_sentiment(body: ModelOutputRequest):
    try:
        if body.model.isalpha():
            return check_sentiment_type_and_get_score(body)
    except ValueError as ev:
        return "Invalid input"


