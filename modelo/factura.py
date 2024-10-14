from modelo.cliente import Cliente

class Factura(Cliente):
    def __init__(self, cliente, nombre, fecha):
        super().__init__(cliente)
        self.nombre = nombre
        self.fecha = fecha
        self.listaProducto = []
        self.listaAntibioticos = []
        self.historial = []

    def crearFactura(self):
        factura = {
            'cliente': self.cliente,
            'nombre': self.nombre,
            'fecha': self.fecha,
            'productos': self.listaProducto,
            'antibioticos': self.listaAntibioticos
        }
        self.historial.append(factura)
        return factura

    def mostrarHistorial(self):
        for factura in self.historial:
            print(factura)

    def cantidadProductos(self):
        return len(self.listaProducto)