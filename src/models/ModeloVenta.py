from src.models.entities.venta import Venta


class ModeloVenta:

    @classmethod
    def nueva_venta(self, db, nombre, apellidos, correo, rfc, direccion, total):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO venta(nombre, apellidos, correo, rfc, direccion, total) 
            VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', {5} )""".format(nombre, apellidos, correo, rfc, direccion, total)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def productos(self, db):
        try:
            cursor = db.connection.cursor()
            query = """SELECT id_nueva_venta, nombre, apellidos, correo, rfc, direccion, total FROM venta"""
            cursor.execute(query)
            data = cursor.fetchall()
            ventas = []
            for v in data:
                venta = Venta(v[0], v[1], v[2], v[3], v[4], v[5], v[6])
                ventas.append(venta)
            return ventas
        except Exception as ex:
            raise Exception(ex)
