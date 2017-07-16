import os
import random
import string
import hashlib
from datetime import datetime

from app.model.cdn import Cdn
from app.model.resource import Resource
from app.ext.db import Session
from app.utils.qiniu_tool import QiniuTool
from app.utils.error import CdnNotFound, FileTypeError
from app.config import get_config_obj

config_obj = get_config_obj()
STATIC_PATH = os.path.join(config_obj.PROJECT_PATH, "static/img")


def put_file(user_id, cdn_type, file):
    file_type = file.type.split("/")
    if len(file_type) == 2 and file_type[0] == "image":
        file_type = file_type[1]
    else:
        raise FileTypeError

    session = Session()
    sha1obj = hashlib.sha1()
    sha1obj.update(file.body)
    hash_code = sha1obj.hexdigest()

    resource = session.query(Resource).filter_by(hash_code=hash_code).first()
    if resource:
        return resource

    file_path = put_file_to_localhost(file, hash_code, file_type)
    file_url = put_file_to_cdn(user_id, cdn_type, file_path, file_type)

    resource = Resource(file_url, creator=user_id)
    session.add(resource)
    session.commit()

    return resource


def get_file_name(file_type):
    now = datetime.now()
    return "{year}/{month}/{day}-{time}-{random}.{file_type}".format(
        year=now.year,
        month=now.month,
        day=now.day,
        time=now.time(),
        random=random.sample(string.ascii_uppercase, 4),
        file_type=file_type,
    )


def put_file_to_cdn(user_id, cdn_type, file_path, file_type):
    session = Session()
    cdn_config = session.query(Cdn).filter_by(cdn_type=cdn_type, user_id=user_id).first()
    if not cdn_config:
        raise CdnNotFound(cdn_type)

    file_url = put_file_to_qiniu(cdn_config, file_path, file_type)

    return file_url


def put_file_to_qiniu(cdn_config, file_path, file_type):
    tool = QiniuTool(cdn_config.qiniu_access_key, cdn_config.qiniu_secret_key, cdn_config.qiniu_bucket_name)
    file_name = get_file_name(file_type)
    result = tool.put_file(file_name, file_path)
    file_url = result['url']
    file_url = "{prefix}{path}{suffix}".format(
        prefix=cdn_config.url_prefix,
        path=file_url,
        suffix=cdn_config.url_suffix,
    )
    return file_url


def put_file_to_localhost(file, hash_code, file_type):
    file_name = "PIC_" + hash_code
    file_name += ".{type}".format(type=file_type)
    file_path = os.path.join(STATIC_PATH, file_name)
    with open(file_path, "wb")as f:
        f.write(file.body)
    return file_path

