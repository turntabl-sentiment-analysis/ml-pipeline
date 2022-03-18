from flask import Flask
from src.controllers.model_controller import model_blueprint
from src.controllers.textblob_controller import model_blueprint_new
app = Flask(__name__)

app.register_blueprint(model_blueprint, url_prefix="/api/v1")
app.register_blueprint(model_blueprint_new, url_prefix="/textblob/v1")

if __name__ == '__main__':
    app.run(debug=True)