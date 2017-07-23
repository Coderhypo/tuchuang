import uuid
from app.ext.db import model
from sqlalchemy import Column, String, DateTime
from datetime import datetime


class Cdn(model):
    __tablename__ = 'cdn'

    cdn_id = Column(String(64), default=lambda: str(uuid.uuid4()), primary_key=True)
    cdn_type = Column(String(64), index=True)
    qiniu_access_key = Column(String(128))
    qiniu_secret_key = Column(String(128))
    qiniu_bucket_name = Column(String(128))
    url_prefix = Column(String(128))
    url_suffix = Column(String(128))
    user_id = Column(String(64), index=True)

    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, user_id, cdn_type):
        self.user_id = user_id
        self.cdn_type = cdn_type

    def set_qiniu(self, qiniu_access_key, qiniu_secret_key, qiniu_bucket_name):
        self.qiniu_access_key = qiniu_access_key
        self.qiniu_secret_key = qiniu_secret_key
        self.qiniu_bucket_name = qiniu_bucket_name

    def set_url(self, url_prefix, url_suffix):
        self.url_prefix = url_prefix
        self.url_suffix = url_suffix
