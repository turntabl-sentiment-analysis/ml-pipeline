from flask import Blueprint
from flask_pydantic import validate
from kedro_project.src.rest_service.services.python_serivce import get_service_output
from kedro_project.src.rest_service.models.python_service_model import PythonModelOutputRequest, PythonModelOutputResponse


python_model_blueprint = Blueprint('python_service', __name__)


@python_model_blueprint.route("/python_service", methods=["POST"])
@validate()
def predict_sentiment(body: PythonModelOutputRequest):
    return get_service_output(body)
