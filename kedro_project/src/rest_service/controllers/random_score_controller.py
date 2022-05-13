from flask import Blueprint
from flask_pydantic import validate
# from rest_service.services.random_score_service import get_model_output
from kedro_project.src.rest_service.services.random_score_service import get_model_output
# from rest_service.models.random_score_model import ModelOutputRequest
from kedro_project.src.rest_service.models.random_score_model import ModelOutputRequest


random_score_model_blueprint = Blueprint('model', __name__)


@random_score_model_blueprint.route("/sentiment-analysis", methods=["POST"])
@validate()
def get_sentiment(body: ModelOutputRequest):
    try:
        if body.model.isalpha():
            return get_model_output(body)
    except ValueError as ev:
        return "Invalid input"


