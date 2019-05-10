from web_chatroom import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(256),unique=True,nullable=False)
    username = db.Column(db.String(32),unique=True,nullable=False)
    password_hash = db.Column(db.String(128))