from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from codeguild.db import get_db
from.auth import login_required

bp = Blueprint('page_manager', __name__, url_prefix='/codeguild')


@bp.route('/<string:section>/posts', methods=('GET', 'POST'))
@login_required
def load(section):
    db = get_db()

    pos = db.execute('SELECT posts.id_post, posts.first_name, posts.last_surname, posts.created, posts.title, posts.body, COALESCE(COUNT(comments.post_id), 0)'
                     ' FROM posts LEFT JOIN comments ON posts.id_post = comments.post_id'
                     ' GROUP BY posts.id_post'
                     ' HAVING subject=?'
                     ' ORDER BY posts.created DESC', (section,)).fetchall()
    db.close()
    return render_template('container_page.html',  posts=pos)