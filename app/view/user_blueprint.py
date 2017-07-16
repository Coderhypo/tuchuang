from sanic import Blueprint
from sanic.response import html, redirect, json
from jinja2 import Environment, PackageLoader, select_autoescape
from app.forms.loginForm import LoginForm
from app.forms.index import IndexForm
from app.forms.registerForm import RegisterForm

user_blueprint = Blueprint('user_blueprint', url_prefix='user')

# jinjia2 config
env = Environment(
    loader=PackageLoader('app.view.user_blueprint', '../templates'),
    autoescape=select_autoescape(['html', 'xml', 'tpl']))


def template(tpl, **kwargs):
    template = env.get_template(tpl)
    return html(template.render(kwargs))


@user_blueprint.route("/login")
async def login(request):
    form = LoginForm(request)

    return template("user/login.html", form=form)


@user_blueprint.route("/register")
async def register(request):
    form = RegisterForm(request)
    return template("user/register.html", form=form)
