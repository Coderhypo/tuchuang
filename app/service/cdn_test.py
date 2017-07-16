import os

from app.service.put_file import put_file_to_qiniu
from app.config import get_config_obj

config_obj = get_config_obj()
TEST_FILE_PATH = os.path.join(config_obj.PROJECT_PATH, "static/img/TEST.jpeg")
TEST_FILE_TYPE = "jpeg"


def qiniu_test(cdn_config):
    url_path = put_file_to_qiniu(cdn_config, TEST_FILE_PATH, TEST_FILE_TYPE)
    return url_path
