from modelo.productoControl import ProductoControl

class ProductoControlPlagas(ProductoControl):
    def __init__(self, nombre, fabricante, periodo_carencia):
        super().__init__(nombre, fabricante)
        self.periodo_carencia = periodo_carencia

    def mostrarPeriodo(self):
        print(f"El periodo de carencia es de {self.periodo_carencia} días.")