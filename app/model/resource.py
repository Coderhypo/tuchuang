import random
import string
import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime

from app.ext.db import model, Session


class Resource(model):
    __tablename__ = 'resource'
    res_id = Column(String(64), default=lambda: str(uuid.uuid4()), primary_key=True)
    res_url = Column(String(256))
    res_short_url = Column(String(128), index=True)
    hash_code = Column(String(128), index=True)

    creator_id = Column(String(64))
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, res_url, creator=None):
        self.res_url = res_url
        self.creator_id = creator
        self.res_short_url = self.__get_short_url()

    @property
    def markdown(self):
        return "![{name}]({url})".format(name=self.res_id, url=self.res_url)

    @classmethod
    def __get_short_url(cls):
        session = Session()
        short = "".join(random.sample(string.ascii_letters, 10))
        unavailable = True
        while unavailable:
            result = session.query(cls).filter_by(res_short_url=short).first()
            if not result:
                unavailable = False
            short = "".join(random.sample(string.ascii_letters, 10))

        return short
