from flask import Flask
from web_chatroom.auth import auth


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.register_blueprint(auth)
    return app