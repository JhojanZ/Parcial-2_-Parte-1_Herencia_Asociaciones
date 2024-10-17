from modelo.productoControl import ProductoControl

class ProductoControlPlagas(ProductoControl):
    def __init__(self, registro_ica, nombre_producto, frecuencia_aplicacion, valor, periodo_carencia):
        super().__init__(registro_ica, nombre_producto, frecuencia_aplicacion, valor)
        self.__periodo_carencia = periodo_carencia

    @property
    def periodo_carencia(self):
        return self.__periodo_carencia
    
    @periodo_carencia.setter
    def periodo_carencia(self, periodo_carencia):
        self.__periodo_carencia = periodo_carencia

    def mostrarPeriodo(self):
        print(f"El periodo de carencia es de {self.periodo_carencia} días.")