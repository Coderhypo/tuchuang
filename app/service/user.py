from app.ext.db import Session
from app.model.user import User


def check_user_login(user_name, password):
    session = Session()
    user = session.query(User).filter_by(user_name=user_name).first()
    print(user.user_name)
    if user.user_password == password:
        return user
    return None


def add_user(user_name, password):
    session = Session()
    user = session.query(User).filter_by(user_name=user_name).first()
    if not user:
        user = User(user_name, password)
        session.add(user)
        session.commit()
    else:
        return None
