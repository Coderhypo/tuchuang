from app.ext.db import Session
from app.model.cdn import Cdn


def setting_to_cdn(user_id, qiniu_access_key, qiniu_secret_key, qiniu_bucket_name, url_prefix, url_suffix):
    session = Session()
    cdn = session.query(Cdn).filter_by(user_id=user_id, cdn_type="qiniu").first()
    if not cdn:
        cdn = Cdn(user_id, "qiniu")
    cdn.set_qiniu(qiniu_access_key, qiniu_secret_key, qiniu_bucket_name)
    cdn.set_url(url_prefix, url_suffix)

    session.add(cdn)
    session.commit()
    return cdn


def get_cdn_by_type(user_id, cdn_type):
    session = Session()
    cdn = session.query(Cdn).filter_by(user_id=user_id, cdn_type=cdn_type).first()
    cdn = session.query(Cdn).filter_by(user_id=user_id, cdn_type=cdn_type).first()
    return cdn
