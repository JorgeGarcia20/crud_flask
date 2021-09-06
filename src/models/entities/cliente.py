from werkzeug.security import check_password_hash
from flask_login import UserMixin


class Cliente(UserMixin):

    def __init__(self, id, nombre, apellidos, nick, password, correo, rfc, direccion):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.nick = nick
        self.password = password
        self.correo = correo
        self.rfc = rfc
        self.direccion = direccion

    @classmethod
    def check_password(self, encrypted, password):
        return check_password_hash(encrypted, password)
