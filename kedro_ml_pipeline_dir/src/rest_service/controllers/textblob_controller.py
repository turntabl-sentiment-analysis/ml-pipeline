from flask_pydantic import validate
from rest_service.models.models import TextBlobOutputRequest
from rest_service.services.service import get_textblob_output
from flask import Blueprint

model_blueprint_new = Blueprint('textblob', __name__)


@model_blueprint_new.route("/textblob-get-sentiment-score", methods=["POST"])
@validate()
def get_sentiment(body: TextBlobOutputRequest):
    return get_textblob_output(body)
