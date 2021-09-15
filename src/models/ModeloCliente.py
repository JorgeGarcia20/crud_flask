from .entities.cliente import Cliente


class ModeloCliente:
    @classmethod
    def login(self, db, cliente):
        try:
            cursor = db.connection.cursor()
            query = """SELECT id, nick, password
						FROM cliente
						WHERE nick = '{0}'""".format(cliente.nick)
            cursor.execute(query)
            data = cursor.fetchone()

            if data != None:
                match = Cliente.check_password(data[2], cliente.password)
                if match:
                    logged = Cliente(data[0], None, None,
                                     data[1], data[2], None, None, None)
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
            query = f"SELECT id, nombre, apellidos, nick, correo, rfc, direccion FROM cliente WHERE id = {id}"
            cursor.execute(query)
            data = cursor.fetchone()
            logged = Cliente(data[0], data[1], data[2],
                             data[3], None, data[4], data[5], data[6])
            return logged

        except Exception as e:
            raise Exception(e)

    @classmethod
    def registrar(self, db, nombre, apellidos, nick, password, correo, rfc, direccion):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO cliente(nombre, apellidos, nick, password, correo, rfc, direccion) 
            VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')""".format(nombre, apellidos, nick, password, correo, rfc, direccion)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
