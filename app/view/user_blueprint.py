from sanic import Blueprint
from sanic.response import redirect

from app.forms.cdnForm import CdnForm
from app.forms.loginForm import LoginForm
from app.forms.registerForm import RegisterForm
from app.service.cdn import setting_to_cdn, get_cdn_by_type
from app.service.user import check_user_login, add_user
from app.utils.helper import set_current_user

user_blueprint = Blueprint('user_blueprint', url_prefix='user')


@user_blueprint.route("/signup", methods=['GET', 'POST'])
async def signup(request):
    user = request['current_user']
    if user:
        redirect("/")
    form = RegisterForm(request)
    if form.validate_on_submit():
        user = add_user(form.name.data, form.password.data)
        if user:
            response = redirect("/")
            response = set_current_user(response, user)
            return response
    return request["template"]("user/signup.html", form=form)


@user_blueprint.route("/signin", methods=['GET', 'POST'])
async def signin(request):
    form = LoginForm(request)
    if form.validate_on_submit():
        user = check_user_login(form.name.data, form.password.data)
        if user:
            response = redirect("/")
            response = set_current_user(response, user)
            return response
    return request["template"]("user/signin.html", form=form)


@user_blueprint.route("/setting", methods=['GET', 'POST'])
async def setting(request):
    user = request["current_user"]
    if not user:
        return
    form = CdnForm(request)
    cdn = get_cdn_by_type(user_id=user.user_id, cdn_type="qiniu")
    if form.validate_on_submit():
        cdn = setting_to_cdn(user.user_id, form.access_key.data, form.secret_key.data, form.bucket_name.data,
                             form.url_prefix.data,
                             form.url_suffix.data)
    if cdn:
        form.access_key.data = cdn.qiniu_access_key
        form.secret_key.data = cdn.qiniu_secret_key
        form.bucket_name.data = cdn.qiniu_bucket_name
        form.url_prefix.data = cdn.url_prefix
        form.url_suffix.data = cdn.url_suffix
    return request["template"]("user/setting.html", form=form)


@user_blueprint.route("/signout", methods=['GET', 'POST'])
async def signout(request):
    request['current_user'] = None
    response = redirect("/")
    response = set_current_user(response, None)
    return response
