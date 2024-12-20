from modelo.productoControl import ProductoControl

class ControlFertilizantes(ProductoControl):
    def __init__(self, registro_ica, nombre_producto, frecuencia_aplicacion, valor, cantidad, fecha_ultima_aplicacion):
        super().__init__(registro_ica, nombre_producto, frecuencia_aplicacion, valor, cantidad)
        self.__fecha_ultima_aplicacion = fecha_ultima_aplicacion

    @property
    def fecha_ultima_aplicacion(self):
        return self.__fecha_ultima_aplicacion
    
    @fecha_ultima_aplicacion.setter
    def fecha_ultima_aplicacion(self, fecha_ultima_aplicacion):
        self.__fecha_ultima_aplicacion = fecha_ultima_aplicacion
