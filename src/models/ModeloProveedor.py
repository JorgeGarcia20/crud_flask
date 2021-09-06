from src.models.entities.proveedor import Proveedor


class ModeloProveedor:
    @classmethod
    def obtener_proveedores(self, db):
        try:
            cursor = db.connection.cursor()
            query = "SELECT id_proveedor, nombre FROM proveedor"
            cursor.execute(query)
            data = cursor.fetchall()
            provedores = []
            for p in data:
                provedor = Proveedor(p[0], p[1])
                provedores.append(provedor)
            return provedores
        except Exception as ex:
            raise Exception(ex)
