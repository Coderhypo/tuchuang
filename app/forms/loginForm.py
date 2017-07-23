# coding=utf-8
from sanic_wtf import SanicForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms import ValidationError

from app.service.user import get_user_by_name


class LoginForm(SanicForm):
    name = StringField('Name', validators=[DataRequired(u"用户名不能为空")])
    password = PasswordField('Password', validators=[DataRequired(u"密码不能为空")])
    submit = SubmitField("Sign in")

    def validate_password(self, field):
        user = get_user_by_name(self.name.data)
        if not user:
            raise ValidationError("用户名或密码错误")
        if user.user_password == field.data:
            return
        raise ValidationError("用户名或密码错误")

