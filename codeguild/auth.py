from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, session, g
import functools
from . import esse3
from .db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


#
# Login
#
@bp.route('/home', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = esse3.login(username, password)

        error = None
        if user is False:
            error = 'Impossible to Log in'

        if error is not None:
            flash(error)
            session.clear()
            return redirect(url_for('index'))

    return render_template('home.html')


@bp.before_app_request
def load_logged_in_user():
    user_nm = session.get('username')

    if user_nm is None:
        g.user = None
    else:
        g.user = user_nm


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('index'))

        return view(**kwargs)
    return wrapped_view
