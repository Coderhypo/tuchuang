import uuid
from app.ext.db import model
from sqlalchemy import Column, String, DateTime
from datetime import datetime


class User(model):
    __tablename__ = 'user'
    user_id = Column(String(64), default=lambda: str(uuid.uuid4()), primary_key=True)
    user_name = Column(String(64))
    user_password = Column(String(128))

    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self,user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password
