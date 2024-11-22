from modelo.productoControl import ProductoControl

class Factura:
    def __init__(self, fecha, valor_total_compra, productos=[]):
        self.__fecha = fecha
        self.__valor_total_compra = valor_total_compra
        self.__producto_control = productos
        #self.__antibiotico = antibioticos
    
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

    """ @property
    def antibiotico(self):
        return self.__antibiotico """
    
    def asociar_producto_control(self, producto_control):
        self.__producto_control.append(producto_control)

    """ def asociar_antibiotico(self, antibiotico):
        self.__antibiotico.append(antibiotico) """
    
    def realizar_venta(self, producto_control = None, cantidad = 1):
        if producto_control != None:
            self.asociar_producto_control(producto_control)
            self.__valor_total_compra = producto_control.valor * cantidad
            
        """ if antibiotico != None:
            self.asociar_antibiotico(antibiotico)
            self.__valor_total_compra = antibiotico.precio * cantidad """