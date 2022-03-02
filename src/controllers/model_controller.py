from flask import Blueprint
from flask_pydantic import validate

from src.functionalities.model_score import get_model_score
from src.models.models import RequestObject

model_blueprint = Blueprint('model', __name__)


@model_blueprint.route("/sentiment-score", methods=["POST"])
@validate()
def get_sentiment(body: RequestObject):
    return get_model_score(body)
