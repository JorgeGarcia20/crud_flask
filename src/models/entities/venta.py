class Venta:
    def __init__(self, id, nombre, apellidos, correo, rfc, direccion, total):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.rfc = rfc
        self.direccion = direccion
        self.total = total

    def nombre_completo(self):
        return f"{self.nombre} {self.apellidos}"
