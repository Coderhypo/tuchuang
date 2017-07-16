from sanic_wtf import FileAllowed, FileRequired, SanicForm
from wtforms import FileField, SubmitField


class IndexForm(SanicForm):
    image = FileField('Image', validators=[
        FileRequired(message="请添加图片"),
        FileAllowed('bmp gif jpg jpeg png'.split(" "), message="图片格式不支持"),
    ])
    submit = SubmitField("upload")
