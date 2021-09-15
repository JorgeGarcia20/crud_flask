from werkzeug.security import check_password_hash
from flask_login import UserMixin


class Usuario(UserMixin):

    def __init__(self, id, nombre, apellidos, nick, password, correo):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.nick = nick
        self.password = password
        self.correo = correo

    @classmethod
    def check_password(self, encrypted, password):
        return check_password_hash(encrypted, password)
