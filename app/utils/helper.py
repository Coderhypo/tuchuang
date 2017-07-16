import random
import string
from itsdangerous import URLSafeSerializer, BadSignature

from app.ext.db import Session
from app.model.user import User
from app.config import get_config_obj

USER_INFO_COOKIE = "U_I"
config_obj = get_config_obj()
serializer = URLSafeSerializer(config_obj.SECRET_KEY)


def set_current_user(response, user):
    u = {
        "user_id": user.user_id,
        "salt": random.sample(string.ascii_letters, 10),
    }
    cookie = serializer.dumps(u)
    response.cookies[USER_INFO_COOKIE] = cookie
    return response


def get_current_user(request):
    u = request.cookies.get(USER_INFO_COOKIE)

    if not u:
        return None
    try:
        u = serializer.loads(u)
    except BadSignature:
        u = None
    if not u or not u.get("user_id"):
        return None

    session = Session()
    user_id = u.get("user_id")
    user = session.query(User).filter_by(user_id=user_id).first()
    if not user:
        return None
    return user
