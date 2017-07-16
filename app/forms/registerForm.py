# coding=utf-8
from sanic_wtf import SanicForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(SanicForm):
    name = StringField('Name', validators=[DataRequired(u"用户名不能为空")])
    password = PasswordField('Password', validators=[DataRequired(u"密码不能为空")])
    re_password = PasswordField('Repassword', validators=[DataRequired(u"密码不能为空")])
    submit = SubmitField("Register")
