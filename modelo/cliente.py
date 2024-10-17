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
    def agregar_factura(self, factura):
        self.__factura.append(factura)

    def mostrar_todas_facturas(self):
        if not self.__factura:
            print("No hay facturas disponibles.")
            return

        for factura in self.factura:
            factura.mostrar_factura()

    def actualiza_datos(self, nombre, dni):
        if nombre:
            self.nombre = nombre
        if dni:
            self.dni = dni

    def nuevo_cliente(self, nombre, dni):
        return Cliente(nombre, dni)
    
    def agregar_pedido(self, factura):
        self.pedidos.append(factura) 