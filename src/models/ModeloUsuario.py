from .entities.usuario import Usuario


class ModeloUsuario:
    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            query = """SELECT id, nick, password
						FROM usuario
						WHERE nick = '{0}'""".format(usuario.nick)
            cursor.execute(query)
            data = cursor.fetchone()

            if data != None:
                match = Usuario.check_password(data[2], usuario.password)
                if match:
                    logged = Usuario(data[0], None, None,
                                     data[1], data[2], None)
                    return logged
                else:
                    return None
            else:
                return None

        except Exception as e:
            raise Exception(e)

    @classmethod
    def obtener_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            query = f"SELECT id, nombre, apellidos, nick, correo FROM usuario WHERE id = {id}"
            cursor.execute(query)
            data = cursor.fetchone()
            logged = Usuario(data[0], data[1], data[2],
                             data[3], None, data[4])
            return logged

        except Exception as e:
            raise Exception(e)

    @classmethod
    def registrar(self, db, nombre, apellidos, nick, password, correo):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO usuario(nombre, apellidos, nick, password, correo) 
            VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')""".format(nombre, apellidos, nick, password, correo)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
