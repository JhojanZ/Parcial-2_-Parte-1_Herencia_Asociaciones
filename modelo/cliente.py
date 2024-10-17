class Cliente:
    def __init__(self, nombre: str, dni: str):
        self.__nombre = nombre
        self.__dni = dni
        self.__factura= []

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def factura(self):
        return self.__factura
    
    @nombre.setter
    def factura(self, factura):
        self.__factura.append(factura)

''' def consultarClientes(self):
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
        self.pedidos.append(factura) '''