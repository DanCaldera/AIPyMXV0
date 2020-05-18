from flask import Flask  # pylint: disable=import-error
from flask_bootstrap import Bootstrap  # pylint: disable=import-error
from flask_login import LoginManager  # pylint: disable=import-error

from .auth import auth  # pylint: disable=import-error
from .config import Config  # pylint: disable=import-error
from .models import UserModel # pylint: disable=import-error

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app) # pylint: disable=unused-variable

    app.config.from_object(Config)

    login_manager.init_app(app)

    app.register_blueprint(auth)

    return app
