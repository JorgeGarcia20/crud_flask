import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Configuration):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    # MYSQL_HOST = 'localhost'
    # MYSQL_USER = 'root'
    # MYSQL_PASSWORD = 'secret'
    # MYSQL_DB = 'tienda_test2'
    # MAIL_SERVER = 'mstp.googlemail.com'
    # MAIL_POST = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = ''
    # MAIL_PASSOWORD = ''
    # 'config('MAIL_PASSWORD')'


config = {
    'dev': DevelopmentConfig,
    'default': DevelopmentConfig
}
