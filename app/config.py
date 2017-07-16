import os


class Config(object):
    DEBUG = False
    TEST = False

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_PASS = os.getenv("DATABASE_PASS")
    DATABASE_URI = os.getenv("DATABASE_URI")
    DATABASE_PORT = 3306
    DATABASE_DB = os.getenv("DATABASE_DB", "tuchuang")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{USER}:{PASS}@{URI}:{PORT}/{DBNAME}?charset=utf8".format(
        USER=DATABASE_USER,
        PASS=DATABASE_PASS,
        URI=DATABASE_URI,
        PORT=DATABASE_PORT,
        DBNAME=DATABASE_DB,
    )


# development
class DevelopmentConfig(Config):
    DEBUG = True
    TEST = False
    SECRET_KEY = "THIS_A_KEY"


# production
class ProductionConfig(Config):
    SECRET_KEY = os.getenv("SECRET_KEY")


# testing
class TestingConfig(Config):
    TEST = True
    SECRET_KEY = "THIS_A_KEY"


app_config = {
    "DEVELOPMENT": DevelopmentConfig,
    "PRODUCTION": ProductionConfig,
    "TESTING": TestingConfig,
    "DEFAULT": TestingConfig,
}


def get_config_obj():
    """
    Get config class without app context
    :return:
    """
    return app_config[os.getenv("RUNTIME", "DEFAULT")]
