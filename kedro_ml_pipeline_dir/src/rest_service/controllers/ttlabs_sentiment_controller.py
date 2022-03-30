from flask_pydantic import validate
from rest_service.services.ttlabs_sentiment_service import predict
from rest_service.models.ttlabs_sentiment_model import ModelPredictionRequest

from flask import Blueprint

ttlabs_sentiment_model_blueprint= Blueprint('sentiment', __name__)


@ttlabs_sentiment_model_blueprint.route("/sentiment-score", methods=["POST"])
@validate()
def predict_sentiment(body: ModelPredictionRequest):
    return predict(body)

