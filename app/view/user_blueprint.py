from sanic import Blueprint
from sanic.response import html, redirect, json
from sanic.response import redirect
from jinja2 import Environment, PackageLoader, select_autoescape

from app.forms.loginForm import LoginForm
from app.utils.helper import set_current_user, get_current_user
from app.forms.registerForm import RegisterForm
from app.service.user import check_user_login, add_user

user_blueprint = Blueprint('user_blueprint', url_prefix='user')

# jinjia2 config
env = Environment(
    loader=PackageLoader('app.view.user_blueprint', '../templates'),
    autoescape=select_autoescape(['html', 'xml', 'tpl']))


def template(tpl, **kwargs):
    template = env.get_template(tpl)
    return html(template.render(kwargs))


@user_blueprint.route("/login", methods=['GET', 'POST'])
async def login(request):
    form = LoginForm(request)
    if form.validate_on_submit():
        user = check_user_login(form.name.data, form.password.data)
        if user:
            response = redirect("/")
            response = set_current_user(response, user)
            return response
    return template("user/login.html", form=form)


@user_blueprint.route("/register", methods=['GET', 'POST'])
async def register(request):
    user = get_current_user(request)
    if user:
        redirect("/")
    form = RegisterForm(request)
    if form.validate_on_submit():
        user = add_user(form.name.data, form.password.data)
        if user:
            response = redirect("/")
            response = set_current_user(response, user)
            return response
    return template("user/register.html", form=form)
