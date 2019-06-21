from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from codeguild.db import get_db
from.auth import login_required

bp = Blueprint('view_post', __name__, url_prefix='/view')

id_to_display = 0

post=None
comments = None

@bp.route('/<int:view_id>', methods=('GET', 'POST'))
@login_required
def viewpost(view_id):
    global id_to_display, post, comments
    id_to_display = view_id

    db = get_db()
    post = db.execute('SELECT id_post, first_name, last_surname, created, title, body '
                      ' FROM posts WHERE id_post=?', (view_id,)).fetchone()

    comments = db.execute('SELECT comm_first_name, comm_last_surname, comm_created, comm_body'
                          ' FROM comments WHERE post_id=?', (view_id,)).fetchall()

    db.close()
    if post is not None:
        return render_template('view_post.html', post=post, comments=comments)
    else:
        return redirect(url_for('home.load'))


@bp.route('/created', methods=('GET', 'POST'))
@login_required
def create_comment():
    body = request.form['body']
    username = session.get('userFirstName')
    surname = session.get('userLastSurname')

    global id_to_display, post, comments

    error = None

    if not body:
        error = 'Body required'

    if error is None:
        db = get_db()
        db.execute('INSERT into comments (post_id, comm_body, comm_first_name, comm_last_surname) VALUES(?, ?, ?, ?)' , (id_to_display, body, username, surname))
        db.commit()

        post = db.execute('SELECT id_post, first_name, last_surname, created, title, body '
                          ' FROM posts WHERE id_post=?', (id_to_display,)).fetchone()

        comments = db.execute('SELECT comm_first_name, comm_last_surname, comm_created, comm_body'
                              ' FROM comments WHERE post_id=?', (id_to_display,)).fetchall()

        db.close()
        if post is not None:
            return render_template('view_post.html', post=post, comments=comments)
    return redirect(url_for('home.load'))
