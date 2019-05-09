from flask import Blueprint
from flask import render_template
from flask import request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', "POST"],endpoint='login')
def login():
    if request.method == 'GET':
        return render_template('login.html')


@auth.route('/register', methods=['GET', "POST"],endpoint='register')
def register():
    if request.method == 'GET':
        return render_template('register.html')