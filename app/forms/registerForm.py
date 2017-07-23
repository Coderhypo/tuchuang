# coding=utf-8
from sanic_wtf import SanicForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError

from app.service.user import get_user_by_name


class RegisterForm(SanicForm):
    name = StringField('Name', validators=[DataRequired(u"用户名不能为空")])
    password = PasswordField('Password', validators=[DataRequired(u"密码不能为空")])
    re_password = PasswordField('Repassword', validators=[DataRequired(u"密码不能为空"),
                                                          EqualTo("password", "两次密码不一致")])
    submit = SubmitField("Register")

    def validate_name(self, field):
        if get_user_by_name(field.data):
            raise ValidationError("用户名已存在")
        return
