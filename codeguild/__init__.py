import os
from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='K3msfk86@!wefdfnab3%&sKJF',
        DATABASE=os.path.join(app.instance_path, 'codeguild.sqlite'),
    )

    @app.route('/')
    def index():
        return render_template('auth.html')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import home
    app.register_blueprint(home.bp)

    from . import create_post
    app.register_blueprint(create_post.bp)

    from . import view_post
    app.register_blueprint(view_post.bp)

    from . import page_manager
    app.register_blueprint(page_manager.bp)

    return app
