class Cliente:
    def __init__(self, nombre: str, dni: str):
        self.nombre = nombre
        self.dni = dni
        self.pedidos = []

    def consultarClientes(self):
        pass

    def buscarCliente(self, dni: str):
        pass

    def actualizaDatos(self, nombre: str = None, dni: str = None):
        if nombre:
            self.nombre = nombre
        if dni:
            self.dni = dni

    def nuevoCliente(self, nombre: str, dni: str):
        return Cliente(nombre, dni)
    
    def agregarPedido(self, factura):
        self.pedidos.append(factura)