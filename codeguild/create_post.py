from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from codeguild.db import get_db
from.auth import login_required

bp = Blueprint('create_post', __name__, url_prefix='/create')


@bp.route('/', methods=('GET', 'POST'))
@login_required
def load():
    return render_template('create_post.html')


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create_post():
    title = request.form['title']
    body = request.form['body']
    username = session.get('userFirstName')
    surname = session.get('userLastSurname')
    sub = request.form['sezione']

    error = None
    if not title:
        error = 'Title required'
    if not body:
        error = 'Body required'

    if error is None:
        db = get_db()
        db.execute('INSERT into posts (title, body, first_name, last_surname, subject) VALUES(?, ?, ?, ?, ?)' , (title, body, username, surname, sub))
        db.commit()

        return redirect(url_for('page_manager.load', section=sub))
    flash(error)
    return render_template('create_post.html')
