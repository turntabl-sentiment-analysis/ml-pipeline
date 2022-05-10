from flask import Flask
from rest_service.controllers.random_score_controller import random_score_model_blueprint
from rest_service.controllers.textblob_controller import textblob_model_blueprint
from rest_service.controllers.ttlabs_sentiment_controller import ttlabs_sentiment_model_blueprint
from rest_service.controllers.python_service_controller import python_model_blueprint

app = Flask(__name__)

app.register_blueprint(random_score_model_blueprint, url_prefix="/api/v1")
app.register_blueprint(textblob_model_blueprint, url_prefix="/textblob/v1")
app.register_blueprint(ttlabs_sentiment_model_blueprint, url_prefix="/sentiment/v1")
app.register_blueprint(python_model_blueprint, url_prefix = "/pythonservice/v1")


def run():
    app.run(debug=True)
