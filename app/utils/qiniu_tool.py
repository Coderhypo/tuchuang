from qiniu import Auth, put_file, etag

from app.utils.error import CdnError


class QiniuTool(object):
    def __init__(self, access_key, secret_key, bucket_name):
        self.q = Auth(access_key, secret_key)
        self.bucket_name = bucket_name

    def get_token(self, file_name):
        token = self.q.upload_token(self.bucket_name, file_name, 3600)
        return token

    def put_file(self, file_name, file_path):
        ret, info = put_file(self.get_token(file_name), file_name, file_path)

        if info.status_code // 100 != 2:
            raise CdnError("Upload error, Qiniu return status code: {code}.".format(code=info.status_code))
        if ret['hash'] != etag(file_path):
            raise CdnError("Hash does not match.")

        return dict(url=ret["key"], hash=ret["hash"])

