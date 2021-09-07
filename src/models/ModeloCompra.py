class ModeloCompra():

    @classmethod
    def comprar(self, db, id_producto, id_cliente):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO compra(id_producto, id_cliente) VALUES ('{0}', '{1}')""".format(
                id_producto, id_cliente)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
