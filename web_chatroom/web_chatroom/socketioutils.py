from app import socketio
from flask_socketio import emit
from flask_login import current_user
from web_chatroom import models
from web_chatroom import db
from lxml.html.clean import clean_html
from flask import render_template
@socketio.on('new_message')
def new_message(content):
    print(content)
    message = models.Message(author=current_user._get_current_object(),content=clean_html(content))
    db.session.add(message)
    db.session.commit()
    emit('new_message',{'message_html':render_template('message.html',message=message)},broadcast=True)
