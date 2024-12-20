from modelo.productoControl import ProductoControl
from CRUD.crudProductos import ProductoControlCrud

class ControladorProductos:
    def __init__(self):
        self.producto_crud = ProductoControlCrud()

    def agregar_producto(self, **kwargs):
        try:
            self.producto_crud.crear_producto(kwargs)
            return True  
        except ValueError as e:
            print(e)
            return False  

    def obtener_productos(self):
        return self.producto_crud.leer_productos()

    def actualizar_producto(self, **kwargs):
        try:
            self.producto_crud.actualizar_producto(kwargs)
            return True
        except ValueError as e:
            print(e)
            return False

    def eliminar_producto(self, registro_ica):
        try:
            self.cliente_crud.eliminar_cliente(registro_ica)
            return True
        except ValueError as e:
            print(e)
            return False
        
    def obtener_lista_productos(self):
        try:
            lista_productos = self.productos_crud.obtener_lista_productos()
            return lista_productos
        except Exception as e:
            print(f"Error al obtener la lista de productos: {e}")
            return []