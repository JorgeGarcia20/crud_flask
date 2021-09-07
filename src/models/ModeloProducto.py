from src.models.entities.categoria import Categoria
from src.models.entities.producto import Producto

from src.models.entities.proveedor import Proveedor


class ModeloProducto:

    @classmethod
    def agregar_producto(self, db, nombre, marca, id_proveedor, id_categoria, precio):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO producto(nombre, marca, id_proveedor, id_categoria, precio) 
                        VALUES ('{0}', '{1}', {2}, {3}, {4})""".format(nombre, marca, id_proveedor, id_categoria, precio)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def consultar_productos(self, db):
        try:
            cursor = db.connection.cursor()
            query = """SELECT producto.id_producto, producto.nombre, producto.marca, proveedor.nombre, categoria.nombre, producto.precio 
                        FROM producto 
                        JOIN proveedor ON producto.id_proveedor = proveedor.id_proveedor 
                        JOIN categoria ON producto.id_categoria = categoria.id_categoria"""
            cursor.execute(query)
            data = cursor.fetchall()
            productos = []
            for p in data:
                producto = Producto(
                    p[0], p[1], p[2], p[3], p[4], p[5])
                productos.append(producto)
            return productos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def consultar_por_id(self, db, id_producto):
        try:
            cursor = db.connection.cursor()
            query = """SELECT id_producto, nombre, marca, id_proveedor, id_categoria, precio
                        FROM producto
                        WHERE id_producto = {0}""".format(id_producto)
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def consultar_producto(self, db, id_producto):
        try:
            cursor = db.connection.cursor()
            query = """SELECT producto.id_producto, producto.nombre, producto.marca, proveedor.nombre, categoria.nombre, producto.precio
                        FROM producto
                        JOIN proveedor ON producto.id_proveedor = proveedor.id_proveedor
                        JOIN categoria ON producto.id_categoria = categoria.id_categoria
                        WHERE id_producto = {0}""".format(id_producto)
            cursor.execute(query)
            data = cursor.fetchone()
            producto = Producto(data[0], data[1], data[2],
                                data[3], data[4], data[5])
            return producto
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def editar_producto(self, db, nombre, marca, id_proveedor, id_categoria, precio, id_producto):
        try:
            cursor = db.connection.cursor()
            query = """ UPDATE producto 
                        SET nombre = '{0}', marca = '{1}', id_proveedor = {2}, id_categoria = {3}, precio = {4}
                        WHERE id_producto = {5}""".format(nombre, marca, id_proveedor, id_categoria, precio, id_producto)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def eliminar_producto(self, db, id_producto):
        try:
            cursor = db.connection.cursor()
            query = "DELETE FROM producto WHERE id_producto = {0}".format(
                id_producto)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
