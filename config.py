class Config(object):
    pass

class ProductionConfig(Config):
    pass

class DeveloperConfig(Config):
    DEBUG = True
