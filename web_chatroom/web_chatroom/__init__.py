from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from web_chatroom.models import *
from web_chatroom.auth import auth
from web_chatroom.chat import chat

def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth)
    app.register_blueprint(chat)
    # 添加配置
    app.config.from_object('web_chatroom.settings.DebugConfig')
    # 读取配置
    db.init_app(app)
    return app