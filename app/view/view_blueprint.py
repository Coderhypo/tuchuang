from sanic import Blueprint
from sanic.response import redirect

from app.forms.index import IndexForm
from app.service.put_file import put_file

view_blueprint = Blueprint('view_blueprint')


@view_blueprint.route("/", methods=['GET', 'POST'])
async def index(request):
    form = IndexForm(request=request)
    user = request.get("current_user")
    if not user:
        return redirect("/user/signin")
    user_id = user.user_id
    if form.validate_on_submit():
        resource = put_file(user_id, "qiniu", form.image.data)
        return request["template"]("picture.html", resource=resource)
    return request["template"]("index.html", form=form)

