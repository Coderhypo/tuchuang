from sanic import Blueprint
from jinja2 import Environment, PackageLoader, select_autoescape
from sanic.response import html

from app.forms.index import IndexForm
from app.service.put_file import put_file

view_blueprint = Blueprint('view_blueprint')

# jinjia2 config
env = Environment(
    loader=PackageLoader('app.view.view_blueprint', '../templates/'),
    autoescape=select_autoescape(['html', 'xml', 'tpl']))


def template(tpl, **kwargs):
    template = env.get_template(tpl)
    return html(template.render(kwargs))


@view_blueprint.route("/", methods=['GET', 'POST'])
async def index(request):
    print("123", request)
    request["user"] = 1
    form = IndexForm(request=request)
    user_id = None
    if form.validate_on_submit():
        put_file(user_id, "qiniu", form.image.data)
    return template("index.html", form=form)
