from modelo.cliente import Cliente
from modelo.factura import Factura

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
        print(self.clientes.__len__())  # Verificación
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
        print(self.clientes)  # Verificación
        if dni not in self.clientes:
            raise ValueError(f"Cliente con DNI {dni} no encontrado.")
        del self.clientes[dni]
        print(f"Cliente con DNI {dni} eliminado correctamente.")

    def buscar_por_cedula(self, dni):
        cliente = self.clientes.get(dni)
    
        if cliente is None:
            print(f"No se encontró un cliente con cédula: {dni}")
        return cliente 
    
    def agregar_factura(self, dni, fecha, valor_total_compra, producto_control):
        if dni not in self.clientes:
            raise ValueError(f"No se encontró un cliente con DNI {dni}.")
        cliente = self.clientes[dni]
        factura = Factura(fecha, valor_total_compra, producto_control)
        cliente.facturas.append(factura)
        print(f"Factura para cliente con DNI {dni} creada correctamente.")
        print("Facturas actualmente en el sistema:", cliente.facturas)

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