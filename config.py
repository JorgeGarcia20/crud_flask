class Configuration:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'secret'
    MYSQL_DB = 'tienda_test'


class DevelopmentConfig(Configuration):
    DEBUG = True


configuration = {
    'dev': DevelopmentConfig,
    'default': DevelopmentConfig
}
