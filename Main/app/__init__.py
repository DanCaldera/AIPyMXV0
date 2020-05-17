from flask import Flask # pylint: disable=import-error
from flask_bootstrap import Bootstrap # pylint: disable=import-error

from .config import Config # pylint: disable=import-error


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)

    return app