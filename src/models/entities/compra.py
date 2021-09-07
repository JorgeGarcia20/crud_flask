import datetime


class Compra:
    def __init__(self, id_compra, id_producto, id_cliente, fecha=None):
        self.id_compra = id_compra
        self.id_producto = id_producto
        self.id_cliente = id_cliente
        self.fecha = fecha

    def fecha_formateada(self):
        return datetime.datetime.strftime(self.fecha, '%d/%m/%Y-%H:%M:%S')
