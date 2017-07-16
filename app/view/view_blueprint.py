from sanic import Blueprint
from jinja2 import Environment, PackageLoader, select_autoescape
from sanic.response import html
from app.forms.index import IndexForm

view_blueprint = Blueprint('view_blueprint')

# jinjia2 config
env = Environment(
    loader=PackageLoader('app.view.view_blueprint', '../templates/'),
    autoescape=select_autoescape(['html', 'xml', 'tpl']))


def template(tpl, **kwargs):
    template = env.get_template(tpl)
    return html(template.render(kwargs))


@view_blueprint.route("/")
async def index(request):
    form = IndexForm(request)
    return template("index.html", form=form)
