import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://karangu:lmzongolo8754@localhost/blog3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    QUOTES_API_KEY = os.environ.get('QUOTES_API_KEY')
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}