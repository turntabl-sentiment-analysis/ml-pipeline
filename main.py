from flask import Flask

from src.controllers.model_controller import model_blueprint

app = Flask(__name__)

app.register_blueprint(model_blueprint, url_prefix="/sentiment")

if __name__ == '__main__':
    app.run(debug=True)
