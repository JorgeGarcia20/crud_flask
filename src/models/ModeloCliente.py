from src.models.entities.cliente import Cliente


class ModeloCliente:

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

    @classmethod
    def login(self, db, cliente):
        try:
            cursor = db.connection.cursor()
            query = """SELECT nick, password FROM cliente WHERE nick = '{0}'""".format(
                cliente.nick)

            cursor.execute(query)
            data = cursor.fetchone()

            if data != None:
                coincide = Cliente.check_password(data[1], cliente.password)
                if coincide:
                    logeado = Cliente(None, None, None,
                                      data[0], data[1], None, None, None)
                    return logeado
                else:
                    return None
            else:
                return None

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def obtener_por_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            query = "SELECT id_cliente, nombre, apellidos, nick, correo, rfc, direccion FROM cliente WHERE id_cliente = '{0}'".format(
                id)
            cursor.execute(query)
            data = cursor.fetchone()
            # return data
            cliente = Cliente(data[0], data[1], data[2],
                              data[3], None, data[4], data[5], data[6])
            return cliente
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            query = """SELECT id_cliente, nombre, apellidos, nick, correo, rfc, direccion FROM cliente WHERE id_cliente = '{0}'""".format(
                id)
            cursor.execute(query)
            data = cursor.fetchone()
            cliente = Cliente(data[0], data[1], data[2],
                              data[3], None, data[4], data[5], data[6])
            return cliente
        except Exception as ex:
            raise Exception(ex)
