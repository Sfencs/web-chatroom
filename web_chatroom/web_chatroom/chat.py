from flask import Blueprint
from flask import render_template,flash,redirect,url_for
from flask import request



chat = Blueprint('chat', __name__)

@chat.route('/chat', methods=['GET', "POST"],endpoint='chat')
def chatroom():
    if request.method == 'GET':
        return render_template('chatroom.html')


