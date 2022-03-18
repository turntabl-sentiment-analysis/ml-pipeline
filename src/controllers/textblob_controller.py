from flask_pydantic import validate
from src.models.models import TextBlobOutputRequest
from src.services.service import get_textblob_output
from flask import Blueprint

model_blueprint_new = Blueprint('textblob', __name__)


@model_blueprint_new.route("/textblob-get-sentiment-score", methods=["POST"])
@validate()
def get_sentiment(body: TextBlobOutputRequest):
    return get_textblob_output(body)
