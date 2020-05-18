from flask_wtf import FlaskForm # pylint: disable=import-error
from wtforms.fields import StringField, PasswordField, SubmitField # pylint: disable=import-error
from wtforms.validators import DataRequired # pylint: disable=import-error


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')