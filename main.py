from distutils.log import debug
from kedro_project.src.rest_service.services import flask_run

if __name__ == '__main__':
    flask_run.run()