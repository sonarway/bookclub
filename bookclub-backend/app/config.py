import os

# ваще пока не понимаю как тут все нормально организовать на локальном серваке, надо разобраться с БД, пока что sqlite
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///bookclub.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
