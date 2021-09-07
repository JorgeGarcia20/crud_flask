from .entities.venta import Venta


class ModeloCompra():

    @classmethod
    def vender(self, db, id_producto, id_cliente):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO compra(id_producto, id_cliente) VALUES ('{0}', '{1}')""".format(
                id_producto, id_cliente)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def consultar_productos_cliente(self, db, id_cliente):
        try:
            cursor = db.connection.cursor()
            query = """SELECT producto.nombre, categoria.nombre, producto.precio, fecha FROM compra
                         JOIN producto ON compra.id_producto = producto.id_producto
                         JOIN categoria ON producto.id_categoria = categoria.id_categoria
                         WHERE id_cliente = {0}""".format(id_cliente)
            cursor.execute(query)
            data = cursor.fetchall()
            ventas = []
            for v in data:
                venta = Venta(v[0], v[1], v[2], v[3])
                ventas.append(venta)
            return ventas
        except Exception as ex:
            raise Exception(ex)
