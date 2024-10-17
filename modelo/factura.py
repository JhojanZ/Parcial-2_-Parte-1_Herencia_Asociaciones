from modelo.productoControl import ProductoControl
from modelo.antibioticos import Antibiotico

class Factura:
    def __init__(self, fecha, valor_total_compra):
        self.__fecha = fecha
        self.__valor_total_compra = valor_total_compra
        self.__producto_control = []
        self.__antibiotico = []
    
    @property
    def fecha(self):
        return self.__fecha
    
    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @property
    def valor_total_compra(self):
        return self.__valor_total_compra
    
    @valor_total_compra.setter
    def valor_total_compra(self, valor_total_compra):
        self.__valor_total_compra = valor_total_compra

    @property
    def producto_control(self):
        return self.__producto_control
    
    @producto_control.setter
    def producto_control(self, producto_control):
        self.__fecha.append(producto_control)

    @property
    def antibiotico(self):
        return self.__antibiotico
    
    @antibiotico.setter
    def antibiotico(self, antibiotico):
        self.__antibiotico = antibiotico

    def asociar_producto_control(self, producto_control):
        self.producto_control = producto_control

    def asociar_antibiotico(self, antibiotico):
        self.antibiotico = antibiotico
        

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