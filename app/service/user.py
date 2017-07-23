from app.ext.db import Session
from app.model.user import User


def get_user_by_name(user_name):
    session = Session()
    user = session.query(User).filter_by(user_name=user_name).first()
    return user


def check_user_login(user_name, password):
    session = Session()
    user = session.query(User).filter_by(user_name=user_name).first()

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
        return user
    else:
        return None