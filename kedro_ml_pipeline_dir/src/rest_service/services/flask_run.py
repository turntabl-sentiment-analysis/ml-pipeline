from flask import Flask
from rest_service.controllers.model_controller import model_blueprint
from rest_service.controllers.textblob_controller import model_blueprint_new

app = Flask(__name__)

app.register_blueprint(model_blueprint, url_prefix="/api/v1")
app.register_blueprint(model_blueprint_new, url_prefix="/textblob/v1")


def run():
    app.run(debug=True)
