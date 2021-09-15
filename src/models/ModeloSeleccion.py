from src.models.entities.producto import Producto


class ModeloSeleccion:
    @classmethod
    def producto_seleccionado(self, db, id_producto):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO seleccion(id_producto) VALUES ('{0}')""".format(
                    id_producto)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def detalle_producto(self, db):
        try:
            cursor = db.connection.cursor()
            query = """SELECT producto.nombre, categoria.nombre, producto.precio FROM seleccion JOIN producto ON seleccion.id_producto = producto.id_producto JOIN categoria ON producto.id_categoria = categoria.id_categoria"""
            cursor.execute(query)
            data = cursor.fetchall()
            productos = []
            for p in data:
                producto = Producto(
                    None, p[0], None, None, p[1], p[2])
                productos.append(producto)
            return productos

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def eliminar_seleccion(self, db, id):
        try:
            cursor = db.connection.cursor()
            query = "DELETE FROM seleccion WHERE id_seleccion = {0}".format(id)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def vaciar_tabla(self, db):
        try:
            cursor = db.connection.cursor()
            query = "TRUNCATE TABLE seleccion"
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
