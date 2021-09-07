from decouple import config


class Configuration:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'


class DevelopmentConfig(Configuration):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'secret'
    MYSQL_DB = 'tienda_test'
    MAIL_SERVER = 'mstp.googlemail.com'
    MAIL_POST = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'fulanotest00@gmail.com'
    MAIL_PASSOWORD = 'MySuperSecret'
    # 'config('MAIL_PASSWORD')'


configuration = {
    'dev': DevelopmentConfig,
    'default': DevelopmentConfig
}
