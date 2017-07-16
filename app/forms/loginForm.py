# coding=utf-8
from sanic_wtf import SanicForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(SanicForm):
    name = StringField('Name', validators=[DataRequired(u"用户名不能为空")])
    password = PasswordField('Password', validators=[DataRequired(u"密码不能为空")])
    submit = SubmitField("Sign in")
