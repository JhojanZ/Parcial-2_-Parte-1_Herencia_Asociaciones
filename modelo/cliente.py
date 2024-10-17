class Cliente:
    def __init__(self, nombre, dni):
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
    
    @factura.setter
    def factura(self, factura):
        self.__factura.append(factura)

    def agregar_factura(self, factura):
        self.__facturas.append(factura)

    def mostrar_facturas(self):
        if not self.__facturas:
            print("No hay facturas del Cliente", self.__nombre)
        else: 
            for facturas in self.__factura:
                print(facturas)

