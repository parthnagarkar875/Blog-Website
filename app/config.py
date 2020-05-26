from app import credentials

class Config:
    SECRET_KEY = credentials.secret_key
    SQLALCHEMY_DATABASE_URI = credentials.db_uri
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = credentials.email
    MAIL_PASSWORD = credentials.password
