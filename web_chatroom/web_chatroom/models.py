from web_chatroom import db
import hashlib
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin,db.Model):

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(256),unique=True,nullable=False)
    username = db.Column(db.String(32),unique=True,nullable=False)
    password_hash = db.Column(db.String(128))
    avatar_url = db.Column(db.String(256))
    messages = db.relationship('Message',back_populates='author',cascade='all')

    def __init__(self,**kwargs):
        super(User,self).__init__(**kwargs)
        if self.email is not None and self.avatar_url is None:
            self.avatar_url = 'https://gravatar.com/avatar/'+hashlib.md5(self.email.encode('utf-8')).hexdigest()+'?d=identicon'


class Message(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.utcnow,index=True)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship('User',back_populates='messages')


