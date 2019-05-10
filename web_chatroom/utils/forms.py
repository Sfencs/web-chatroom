#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wtforms import Form
from wtforms.fields import simple,html5
from wtforms import validators
from wtforms import widgets



class LoginForm(Form):
    username = simple.StringField(
        validators=[
            validators.DataRequired(message='用户名不能为空.')
        ],
        widget=widgets.TextInput(),

    )
    password = simple.PasswordField(
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            validators.Length(min=8, message='密码长度必须大于%(min)d'),

        ],
        widget=widgets.PasswordInput(),
    )

class RegisterForm(Form):
    username = simple.StringField(
        validators=[
            validators.DataRequired(message='用户名不能为空.')
        ],
        widget=widgets.TextInput(),

    )
    password = simple.PasswordField(
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            validators.Length(min=8, message='密码长度必须大于%(min)d'),


        ],
        widget=widgets.PasswordInput(),
    )
    email = html5.EmailField(
        label='邮箱',
        validators=[
            validators.DataRequired(message='邮箱不能为空.'),
            validators.Email(message='邮箱格式错误')
        ],
        widget=widgets.TextInput(input_type='email'),
    )



