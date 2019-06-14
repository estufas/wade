# config.py

class Config(object):
    """
    Common configurations
    """
    MONGO_URI = "mongodb+srv://dbUser:<ADvTSJkx6pi3hcN>@wade-zd2os.mongodb.net/test?retryWrites=true"
    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    MONGO_URI = "mongodb+srv://dbUser:<ADvTSJkx6pi3hcN>@wade-zd2os.mongodb.net/test?retryWrites=true"


class ProductionConfig(Config):
    """
    Production configurations
    """
<<<<<<< HEAD
=======
    MONGO_URI = "mongodb+srv://dbUser:<ADvTSJkx6pi3hcN>@wade-zd2os.mongodb.net/test?retryWrites=true"
    DEBUG = False
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
