from flask import Blueprint
from flask import render_template,flash,redirect,url_for
from flask import request
from flask_login import current_user, login_required
from web_chatroom import models
from web_chatroom import db

chat = Blueprint('chat', __name__)


@chat.route('/chat', methods=['GET', "POST"],endpoint='chat')
@login_required
def chatroom():
    if request.method == 'GET':
        message_list = db.session.query(models.Message).order_by(models.Message.id).all()
        message_list.reverse()
        message_list = message_list[:9]
        message_list.reverse()
        return render_template('chatroom.html',message_list=message_list)


