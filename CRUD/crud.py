from modelo.cliente import Cliente
from modelo.productoControl import ProductoControl

class ClienteCrud:
    def __init__(self):
        self.clientes = {}

    def crear_cliente(self, nombre, dni):
        if dni in self.clientes:
            raise ValueError(f"Cliente con DNI {dni} ya existe.")
        cliente = Cliente(nombre, dni)
        self.clientes[dni] = cliente
        print(f"Cliente {nombre} creado correctamente.")

    def leer_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes.values():
                print(f"Cliente: {cliente.nombre}, DNI: {cliente.dni}")

    def actualizar_cliente(self, dni, nombre=None):
        if dni not in self.clientes:
            raise ValueError(f"Cliente con DNI {dni} no encontrado.")
        if nombre:
            self.clientes[dni].nombre = nombre
        print(f"Cliente con DNI {dni} actualizado correctamente.")

    def eliminar_cliente(self, dni):
        if dni not in self.clientes:
            raise ValueError(f"Cliente con DNI {dni} no encontrado.")
        del self.clientes[dni]
        print(f"Cliente con DNI {dni} eliminado correctamente.")


class ProductoControlCrud:
    def __init__(self):
        self.productos = {}

    def crear_producto(self, registro_ica, nombre_producto, frecuencia_aplicacion, valor, cantidad):
        if registro_ica in self.productos:
            raise ValueError(f"Producto con registro ICA {registro_ica} ya existe.")
        producto = ProductoControl(registro_ica, nombre_producto, frecuencia_aplicacion, valor, cantidad)
        self.productos[registro_ica] = producto
        print(f"Producto {nombre_producto} creado correctamente.")

    def leer_productos(self):
        if not self.productos:
            print("No hay productos registrados.")
        else:
            for producto in self.productos.values():
                print(f"Producto: {producto.nombre_producto}, Registro ICA: {producto.registro_ica}")

    def actualizar_producto(self, registro_ica, nombre_producto=None, valor=None, cantidad=None):
        if registro_ica not in self.productos:
            raise ValueError(f"Producto con registro ICA {registro_ica} no encontrado.")
        producto = self.productos[registro_ica]
        if nombre_producto:
            producto.nombre_producto = nombre_producto
        if valor is not None:
            producto.valor = valor
        if cantidad is not None:
            producto.cantidad = cantidad
        print(f"Producto con registro ICA {registro_ica} actualizado correctamente.")

    def eliminar_producto(self, registro_ica):
        if registro_ica not in self.productos:
            raise ValueError(f"Producto con registro ICA {registro_ica} no encontrado.")
        del self.productos[registro_ica]
        print(f"Producto con registro ICA {registro_ica} eliminado correctamente.")


class CrudManager:
    def __init__(self):
        self.cliente_crud = ClienteCrud()
        self.producto_crud = ProductoControlCrud()

    def crear_cliente(self, nombre, dni):
        self.cliente_crud.crear_cliente(nombre, dni)

    def leer_clientes(self):
        self.cliente_crud.leer_clientes()

    def actualizar_cliente(self, dni, nombre=None):
        self.cliente_crud.actualizar_cliente(dni, nombre)

    def eliminar_cliente(self, dni):
        self.cliente_crud.eliminar_cliente(dni)

    def crear_producto(self, registro_ica, nombre_producto, frecuencia_aplicacion, valor, cantidad):
        self.producto_crud.crear_producto(registro_ica, nombre_producto, frecuencia_aplicacion, valor, cantidad)

    def leer_productos(self):
        self.producto_crud.leer_productos()

    def actualizar_producto(self, registro_ica, nombre_producto=None, valor=None, cantidad=None):
        self.producto_crud.actualizar_producto(registro_ica, nombre_producto, valor, cantidad)

    def eliminar_producto(self, registro_ica):
        self.producto_crud.eliminar_producto(registro_ica)


if __name__ == "__main__":
    manager = CrudManager()

    # Pruebas con Cliente
    nombre_cliente = "Juan Perez"
    dni = "12345678"
    manager.crear_cliente(nombre_cliente, dni)
    manager.leer_clientes()
    manager.actualizar_cliente(dni, nombre="Juan P.")
    manager.leer_clientes()
    manager.eliminar_cliente(dni)
    manager.leer_clientes()
    

    print()

    # Pruebas con ProductoControl
    id = "001"
    producto = "Insecticida"
    manager.crear_producto(id, producto, "Semanal", 1500, 10)
    manager.leer_productos()
    manager.actualizar_producto(id, nombre_producto="Insecticida Plus", valor=1600)
    manager.leer_productos()
    manager.eliminar_producto(id)
    manager.leer_productos()