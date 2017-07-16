class BaseError(Exception):
    error_code = 500
    error_id = "INTERNAL_ERROR"
    error_message = "something wrong."

    def __repr__(self):
        return "<{err_id} {err_code}>: {err_msg}".format(
            err_id=self.error_id,
            err_code=self.error_code,
            err_msg=self.error_message,
        )


class FileTypeError(BaseError):
    error_code = 400
    error_id = "FILE_TYPE_ERROR"
    error_message = "This is not a legitimate picture."


class CdnNotFound(BaseError):
    error_code = 404
    error_id = "CDN_NOT_FOUND"

    def __init__(self, cdn_type):
        self.error_message = "{cdn_type} config not found.".format(cdn_type=cdn_type)


class CdnError(BaseError):
    error_code = 500
    error_id = "CDN_ERROR"

    def __init__(self, error_message):
        self.error_message = error_message

