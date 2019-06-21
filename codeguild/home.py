from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, session, send_file, g
from.auth import login_required

bp = Blueprint('home', __name__, url_prefix='/home')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@bp.route('/load', methods=('GET', 'POST'))
@login_required
def load():
    return render_template('home.html')



