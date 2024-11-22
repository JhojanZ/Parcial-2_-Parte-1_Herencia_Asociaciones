from CRUD.crudProductos import ProductoControlCrud

class ControladorProductos:
    def __init__(self, clienteproducto_crud):
        self.producto_crud = ProductoControlCrud()

    def agregar_producto(self, **kwargs):
        try:
            self.producto_crud.crear_producto(**kwargs)
            return True  
        except ValueError as e:
            print(e)
            return False  

    def obtener_productos(self):
        return self.producto_crud.leer_productos()

    def actualizar_producto(self, registro_ica, nombre_producto, frecuencia_aplicacion, valor, cantidad):
        try:
            self.producto_crud.actualizar_producto(registro_ica, nombre_producto, frecuencia_aplicacion, valor, cantidad)
            return True
        except ValueError as e:
            print(e)
            return False
        
    def buscar_producto(self, id, accion):
        try:
            producto = self.producto_crud.buscar_producto(id)
            if accion == "Eliminar":
                self.eliminar_producto(id)

            elif accion == "Modificar":
                pass

            return producto
        except ValueError as e:
            print(e)
            return None
        

    def eliminar_producto(self, registro_ica):
        try:
            self.producto_crud.eliminar_producto(registro_ica)
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
         