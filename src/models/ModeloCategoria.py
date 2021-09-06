from src.models.entities.categoria import Categoria


class ModeloCategoria:
    @classmethod
    def obtener_categorias(self, db):
        try:
            cursor = db.connection.cursor()
            query = "SELECT id_categoria, nombre FROM categoria"
            cursor.execute(query)
            data = cursor.fetchall()
            categorias = []
            for c in data:
                categoria = Categoria(c[0], c[1])
                categorias.append(categoria)
            return categorias
        except Exception as ex:
            raise Exception(ex)
