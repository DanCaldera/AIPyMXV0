from flask import Flask # pylint: disable=import-error
from flask_bootstrap import Bootstrap # pylint: disable=import-error

from .config import Config # pylint: disable=import-error
from .auth import auth # pylint: disable=import-error


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app) # pylint: disable=unused-variable

    app.config.from_object(Config)

    app.register_blueprint(auth)

    return app