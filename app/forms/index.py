from sanic_wtf import SanicForm
from sanic_wtf import FileAllowed, FileRequired, SanicForm
from wtforms import FileField, SubmitField, StringField


class IndexForm(SanicForm):
    image = FileField('Image', validators=[
        FileRequired(), FileAllowed('bmp gif jpg jpeg png'.split())])
    submit = SubmitField('Upload')
