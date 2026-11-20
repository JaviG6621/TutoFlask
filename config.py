class Config(object):
    pass

class ProductionConfig(config):
    pass

class DeveloperConfig(config):
    DEBUG = True
