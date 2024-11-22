from modelo.factura import Factura

class FacturaCrud:
    def __init__(self):
        self.facturas = {}

    def crear_factura(self, nombre, dni):
        if dni in self.clientes:
            raise ValueError(f"Cliente con DNI {dni} ya existe.")
        cliente = Cliente(nombre, dni)
        self.clientes[dni] = cliente
        print(f"Cliente {nombre} creado correctamente.")
        print("Clientes actualmente en el sistema:", self.clientes)  # Verificación

    """ def leer_facturas(self):
        print(self.clientes.__len__())  # Verificación
        if not self.clientes:
            return []

        clientes = []
        for cliente in self.clientes.values():
            clientes.append(cliente)
        return clientes """
