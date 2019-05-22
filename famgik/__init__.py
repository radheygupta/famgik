from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_debugtoolbar import DebugToolbarExtension
# from flask_perm import Perm

import os

db = SQLAlchemy()

# login_manager = LoginManager()
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.user_login'

# perm = Perm()

toolbar = DebugToolbarExtension()

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app(test_config=None):

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'dev'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "famgik.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://famgik_admin:famgikadmin12345@localhost/flask_famgik_prod'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.config['SECURITY_REGISTERABLE'] = True
    app.config['SECURITY_PASSWORD_SALT'] = 'dev'

    app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
    app.config['SECURITY_SEND_PASSWORD_CHANGE_EMAIL'] = False
    app.config['SECURITY_SEND_PASSWORD_RESET_EMAIL'] = False
    app.config['SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL'] = False

    db.init_app(app)
    # login_manager.init_app(app)
    # perm.init_app(app)
    toolbar.init_app(app)

    # from .auth import auth
    # app.register_blueprint(auth, url_prefix='/auth')

    from .tools import tools
    app.register_blueprint(tools)

    with app.app_context():
        from . import views

    return app



# from .models import FamgikUser
# #Login Manager
# @login_manager.user_loader
# def load_user(user_id):
#     from .models import FamgikUser
#     return FamgikUser.query.get(user_id)
#
#
# #Perm
# # @perm.current_user_loader(lambda: current_user)
#
# @perm.current_user_loader
# def load_current_user():
#     from .models import FamgikUser
#     if 'user_id' in session:
#         return FamgikUser.query.get(session['user_id'])
#
# @perm.user_loader
# def load_user(user_id):
#     from .models import FamgikUser
#     return FamgikUser.query.get(user_id)


# @perm.users_count_loader
# def load_users_count():
#     from .models import FamgikUser
#     return FamgikUser.query.all()
#
#
# @perm.users_loader
# def load_users(filter_by={}, sort_field='created_at', sort_dir='desc', offset=0, limit=20):
#     from .models import FamgikUser
#     sort = getattr(getattr(FamgikUser, sort_field), sort_dir)()
#     return FamgikUser.query.filter_by(**filter_by).order_by(sort).offset(offset).limit(limit).all()
