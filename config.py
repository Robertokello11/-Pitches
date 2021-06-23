import os

class Config:
    SECRET_KEY = 'Robert11'
    UPLOADED_PHOTOS_DEST ='app/static/images'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Robert11@localhost/pitches'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Robert11@localhost/pitches'

    
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}