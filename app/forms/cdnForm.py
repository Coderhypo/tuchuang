# coding=utf-8
from sanic_wtf import SanicForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CdnForm(SanicForm):
    access_key = StringField('七牛access_key', validators=[DataRequired("access_key不能为空")])
    secret_key = StringField('七牛secret_key', validators=[DataRequired("secret_key不能为空")])
    bucket_name = StringField('bucket_name', validators=[DataRequired("bucket_name不能为空")])
    url_prefix = StringField('url_prefix', validators=[DataRequired("url_prefix不能为空")])
    url_suffix = StringField('url_suffix', validators=[DataRequired("url_suffix不能为空")])

