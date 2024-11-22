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
        print("Clientes actualmente en el sistema:", self.clientes)  # Verificación

    def leer_clientes(self):
        if not self.clientes:
            return []

        clientes = []
        for cliente in self.clientes.values():
            clientes.append(cliente)
        return clientes

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

    def buscar_por_cedula(self, dni):
        cliente = self.clientes.get(dni)
    
        if cliente is None:
            print(f"No se encontró un cliente con cédula: {dni}")
        return cliente 

    def mostrar_facturas(self, cliente):
        if not cliente.facturas:
            print("El cliente no tiene facturas.")
            return

        for factura in cliente.facturas:
            print(f"Factura ID: {factura.id}")
            print(f"Fecha: {factura.fecha}")
            print(f"Total: {factura.total}")
            print("Productos:")
            for producto in factura.productos:
                print(f"  - {producto.nombre_producto}: {producto.cantidad} unidades a {producto.valor} cada una")
                print("\n")


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

    def eliminar_producto(self, registro_ica):
        if registro_ica not in self.productos:
            print(f"Producto con registro ICA {registro_ica} no encontrado.")
        del self.productos[registro_ica]
        print(f"Producto con registro ICA {registro_ica} eliminado correctamente.")
