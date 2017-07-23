# coding=utf-8
from sanic_wtf import SanicForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CdnForm(SanicForm):
    access_key = StringField('Access Key', validators=[DataRequired("access key不能为空")])
    secret_key = StringField('Secret Key', validators=[DataRequired("secret key不能为空")])
    bucket_name = StringField('Bucket Name', validators=[DataRequired("bucket name不能为空")])
    url_prefix = StringField('Prefix', validators=[DataRequired("url 不能为空")])
    url_suffix = StringField('Suffix')

