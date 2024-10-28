from modelo.cliente import Cliente
from modelo.productoControl import ProductoControl
from modelo.factura import Factura
from modelo.control_plagas import ProductoControlPlagas
from modelo.controlFertilizantes import ControlFertilizantes
from modelo.antibioticos import Antibiotico

class CrudManager:
    def __init__(self):
        self.clientes = {}
        self.productos = {}
        self.facturas = {}

    # CRUD para Cliente
    def crear_cliente(self, nombre, dni):
        if dni in self.clientes:
            print(f"Error: Cliente con DNI {dni} ya existe.")
        else:
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
            print(f"Error: Cliente con DNI {dni} no encontrado.")
        else:
            if nombre:
                self.clientes[dni].nombre = nombre
            print(f"Cliente con DNI {dni} actualizado correctamente.")

    def eliminar_cliente(self, dni):
        if dni in self.clientes:
            del self.clientes[dni]
            print(f"Cliente con DNI {dni} eliminado correctamente.")
        else:
            print(f"Error: Cliente con DNI {dni} no encontrado.")

    # CRUD para ProductoControl
    def crear_producto(self, registro_ica, nombre_producto, frecuencia_aplicacion, valor, cantidad):
        if registro_ica in self.productos:
            print(f"Error: Producto con registro ICA {registro_ica} ya existe.")
        else:
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
            print(f"Error: Producto con registro ICA {registro_ica} no encontrado.")
        else:
            producto = self.productos[registro_ica]
            if nombre_producto:
                producto.nombre_producto = nombre_producto
            if valor:
                producto.valor = valor
            if cantidad:
                producto.cantidad = cantidad
            print(f"Producto con registro ICA {registro_ica} actualizado correctamente.")

    def eliminar_producto(self, registro_ica):
        if registro_ica in self.productos:
            del self.productos[registro_ica]
            print(f"Producto con registro ICA {registro_ica} eliminado correctamente.")
        else:
            print(f"Error: Producto con registro ICA {registro_ica} no encontrado.")

    # CRUD para Factura
    def crear_factura(self, dni_cliente, fecha, valor_total_compra):
        if dni_cliente not in self.clientes:
            print(f"Error: Cliente con DNI {dni_cliente} no encontrado.")
            return
        
        factura = Factura(fecha, valor_total_compra)
        self.clientes[dni_cliente].agregar_factura(factura)
        self.facturas[f"{dni_cliente}_{fecha}"] = factura
        print(f"Factura creada para el cliente {dni_cliente} en la fecha {fecha}.")

    def leer_facturas(self):
        if not self.facturas:
            print("No hay facturas registradas.")
        else:
            for key, factura in self.facturas.items():
                print(f"Factura: {key}, Fecha: {factura.fecha}, Valor Total: {factura.valor_total_compra}")

    def actualizar_factura(self, dni_cliente, fecha, valor_total_compra=None):
        key = f"{dni_cliente}_{fecha}"
        if key not in self.facturas:
            print(f"Error: Factura no encontrada para el cliente {dni_cliente} en la fecha {fecha}.")
        else:
            factura = self.facturas[key]
            if valor_total_compra:
                factura.valor_total_compra = valor_total_compra
            print(f"Factura para el cliente {dni_cliente} en la fecha {fecha} actualizada correctamente.")

    def eliminar_factura(self, dni_cliente, fecha):
        key = f"{dni_cliente}_{fecha}"
        if key in self.facturas:
            del self.facturas[key]
            print(f"Factura eliminada para el cliente {dni_cliente} en la fecha {fecha}.")
        else:
            print(f"Error: Factura no encontrada para el cliente {dni_cliente} en la fecha {fecha}.")
