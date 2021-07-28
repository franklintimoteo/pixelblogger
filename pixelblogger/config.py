import os

basedir = os.path.abspath(os.path.dirname(__name__))


class Config:
  SECRET_KEY = os.urandom(16)
  SQLALCHEMY_TRACK_MODIFICATIONS = False


  @staticmethod
  def init_app(app):
    pass

class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
  
class TestingConfig(Config):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///'
  
  
class ProductionConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')

config = {
  'development': DevelopmentConfig,
  'production': ProductionConfig,
  'default': DevelopmentConfig
}