from flask_pydantic import validate
from flask import Blueprint
from rest_service.models.textblob_model import TextBlobOutputRequest
from rest_service.services.textblob_service import get_textblob_output

textblob_model_blueprint = Blueprint('textblob', __name__)


@textblob_model_blueprint.route("/textblob-get-sentiment-score", methods=["POST"])
@validate()
def get_sentiment(body: TextBlobOutputRequest):
    return get_textblob_output(body)
