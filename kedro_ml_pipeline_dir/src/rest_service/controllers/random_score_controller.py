from flask import Blueprint
from flask_pydantic import validate
from rest_service.services.textblob_service import check_sentiment_type_and_get_score
from rest_service.models.random_score_model import ModelOutputRequest


random_score_model_blueprint = Blueprint('model', __name__)


@random_score_model_blueprint.route("/sentiment-analysis", methods=["POST"])
@validate()
def get_sentiment(body: ModelOutputRequest):
    try:
        if body.model.isalpha():
            return check_sentiment_type_and_get_score(body)
    except ValueError as ev:
        return "Invalid input"


