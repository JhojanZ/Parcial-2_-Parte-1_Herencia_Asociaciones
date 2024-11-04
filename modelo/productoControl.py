class ProductoControl:
    def __init__(self, registro_ica, nombre_producto, frecuencia_aplicacion, valor, cantidad):
        self.__registro_ica = registro_ica
        self.__nombre_producto = nombre_producto
        self.__frecuencia_aplicacion = frecuencia_aplicacion
        self.__valor = valor
        self.__cantidad = cantidad

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

    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

