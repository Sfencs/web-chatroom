from flask import Flask,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

from web_chatroom.models import *
from web_chatroom.auth import auth
from web_chatroom.chat import chat




@login_manager.user_loader
def load_user(user_id):

        return db.session.query(models.User).filter(models.User.id==user_id).first()

@login_manager.unauthorized_handler
def unauthorized():

    return redirect(url_for('auth.login'))


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth)
    app.register_blueprint(chat)
    # 添加配置
    app.config.from_object('web_chatroom.settings.DebugConfig')
    # 读取配置
    db.init_app(app)
    login_manager.init_app(app)
    CSRFProtect(app)

    return app