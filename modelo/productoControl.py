from modelo.factura import Factura

class ProductoControl:
    def __init__(self, registro_ica: str, nombre_producto: str, frecuencia_aplicacion: int, valor: float, cantidad: int):
        self.__registro_ica = registro_ica
        self.__nombre_producto = nombre_producto
        self.__frecuencia_aplicacion = frecuencia_aplicacion
        self.__valor = valor

    @property
    def registro_ica(self):
        return self.__registro_ica
    
    @registro_ica.setter
    def registro_ica(self, registro_ica):
        self.__registro_ica = registro_ica

    @property
    def nombre_producto(self):
        return self.__nombre_producto
    
    @nombre_producto.setter
    def nombre_producto(self, nombre_producto):
        self.__nombre_producto = nombre_producto

    @property
    def frecuencia_aplicacion(self):
        return self.__frecuencia_aplicacion
    
    @frecuencia_aplicacion.setter
    def frecuencia_aplicacion(self, frecuencia_aplicacion):
        self.__frecuencia_aplicacion = frecuencia_aplicacion

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    def insertarProducto(self, producto):
        self.productos.append(producto)

    def buscarProductoNombre(self, nombre_producto: str):
        for producto in self.productos:
            if producto.nombre_producto == nombre_producto:
                return producto
        return None

    def buscarProductoRegistro(self, registro_ica: str):
        for producto in self.productos:
            if producto.registro_ica == registro_ica:
                return producto
        return None

    def actualizarProducto(self, registro_ica: str, nombre_producto: str, frecuencia_aplicacion: int, valor: float, cantidad: int):
        producto = self.buscarProductoRegistro(registro_ica)
        if producto:
            producto.nombre_producto = nombre_producto
            producto.frecuencia_aplicacion = frecuencia_aplicacion
            producto.valor = valor
            producto.cantidad = cantidad
            return True
        return False