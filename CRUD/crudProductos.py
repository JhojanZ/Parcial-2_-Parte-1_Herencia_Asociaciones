from modelo.productoControl import ProductoControl

class ProductoControlCrud:
    def __init__(self):
        self.productos = {}

    def crear_producto(self, **datos):
        registro_ica = datos.get('registro_ica')
        nombre_producto = datos.get('nombre_producto')
        frecuencia_aplicacion = datos.get('frecuencia_aplicacion')
        valor = datos.get('valor')
        cantidad = datos.get('cantidad')

        if registro_ica in self.productos:
            raise ValueError(f"Producto con registro ICA {registro_ica} ya existe.")

        producto = ProductoControl(registro_ica, nombre_producto, frecuencia_aplicacion, valor, cantidad)
        self.productos[registro_ica] = producto
        print(f"Producto {nombre_producto} creado correctamente.")
        print(f"Estado actual de productos: {self.productos}")


    def leer_productos(self):
        if not self.productos:
            print("No hay productos registrados.")
            return []
        
        productos = []
        for producto in self.productos.values():
            productos.append(producto)
        return productos

    def actualizar_producto(self, registro_ica, nombre_producto=None, valor=None, cantidad=None):
        if registro_ica not in self.productos:
            print(f"Producto con registro ICA {registro_ica} no encontrado.")
        producto = self.productos[registro_ica]
        if nombre_producto:
            producto.nombre_producto = nombre_producto
        if valor is not None:
            producto.valor = valor
        if cantidad is not None:
            producto.cantidad = cantidad
        print(f"Producto con registro ICA {registro_ica} actualizado correctamente.")

    def buscar_producto(self, registro_ica):
        if registro_ica not in self.productos:
            print(f"Producto con registro ICA {registro_ica} no encontrado.")
            return None
        return self.productos[registro_ica]

    def eliminar_producto(self, registro_ica):
        if registro_ica not in self.productos:
            print(f"Producto con registro ICA {registro_ica} no encontrado.")
        del self.productos[registro_ica]
        print(f"Producto con registro ICA {registro_ica} eliminado correctamente.")
