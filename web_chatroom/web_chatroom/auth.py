from flask import Blueprint
from flask import render_template,flash,redirect,url_for
from flask import request
from web_chatroom import models
from web_chatroom import db
from flask_login import login_user,logout_user,login_required
import hashlib
from utils import forms



auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', "POST"],endpoint='login')
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = forms.LoginForm(formdata=request.form)
        if form.validate():
            password_hash = hashlib.md5(form.data['password'].encode('utf-8')).hexdigest()
            user_obj = db.session.query(models.User).filter(db.and_(models.User.username == form.data['username'],
                                                                models.User.password_hash == password_hash)).first()
            if user_obj:
                login_user(user_obj)
                return redirect(url_for('chat.chat'))
            else:
                flash('用户名或密码错误')
                return redirect(url_for('auth.login'))
                pass
        else:
            for error in form.errors:
                flash(form.errors[error][0])
            return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', "POST"],endpoint='register')
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        form = forms.RegisterForm(formdata=request.form)
        if form.validate():
            count = db.session.query(models.User).filter(db.or_(models.User.username == form.data['username'],
                                                        models.User.email == form.data['email'])).count()
            if count:
                flash('用户名或邮箱已存在')
                return redirect(url_for('auth.register'))
            else:
                password_hash = hashlib.md5(form.data['password'].encode('utf-8')).hexdigest()
                db.session.add(models.User(username=form.data['username'],
                                           email=form.data['email'],
                                           password_hash=password_hash))
                db.session.commit()
                db.session.close()
                flash('注册成功')
                return redirect(url_for('auth.login'))
        else:
            for error in form.errors:
                flash(form.errors[error][0])
            return redirect(url_for('auth.register'))

@login_required
@auth.route('/logout', methods=['GET', "POST"],endpoint='logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
