from sanic import Sanic

from app.config import get_config_obj


def create_app():
    app = Sanic(__name__)
    config_obj = get_config_obj()
    app.config.from_object(config_obj)

    return app
