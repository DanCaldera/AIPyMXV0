from flask import render_template, session, redirect, url_for, flash # pylint: disable=import-error

from app.forms import LoginForm

from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Nombre de usario registrado con éxito!')

        return redirect(url_for('index'))
    return render_template('login.html', **context)