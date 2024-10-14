from modelo.factura import Factura

class ProductoControl(Factura):
    def __init__(self, registro_ica: str, nombre_producto: str, frecuencia_aplicacion: int, valor: float, cantidad: int):
        self.registro_ica = registro_ica
        self.nombre_producto = nombre_producto
        self.frecuencia_aplicacion = frecuencia_aplicacion
        self.valor = valor
        self.cantidad = cantidad
        self.productos = []

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