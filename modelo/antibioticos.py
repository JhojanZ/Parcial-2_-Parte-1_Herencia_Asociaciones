from modelo.factura import Factura

class Antibiotico:
    def __init__(self, id_factura: int, nombre_antibiotico: str, dosis: float, tipo_animal: str, precio: float, cantidad: int):
        super().__init__(id_factura)
        self.__nombre_antibiotico = nombre_antibiotico
        self.__dosis = dosis
        self.__tipo_animal = tipo_animal
        self.__precio = precio

    @property
    def nombre_antibiotico(self):
        return self.__nombre_antibiotico
    
    @nombre_antibiotico.setter
    def nombre_antibiotico(self, nombre_antibiotico):
        self.__nombre_antibiotico = nombre_antibiotico

    @property
    def dosis(self):
        return self.__dosis
    
    @dosis.setter
    def dosis(self, dosis):
        self.__dosis = dosis

    @property
    def tipo_animal(self):
        return self.__tipo_animal
    
    @tipo_animal.setter
    def tipo_animal(self, tipo_animal):
        self.__tipo_animal = tipo_animal

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    def insertarAntibiotico(self, nombre_producto: str, dosis: float, tipo_animal: str, precio: float, cantidad: int):
        self.nombre_producto = nombre_producto
        self.dosis = dosis
        self.tipo_animal = tipo_animal
        self.precio = precio
        self.cantidad = cantidad
        print(f"Antibiotico {nombre_producto} insertado correctamente.")

    def buscarAntibiotico(self, nombre_producto: str):
        if self.nombre_producto == nombre_producto:
            return self
        else:
            print(f"Antibiotico {nombre_producto} no encontrado.")
            return None

    def actualizarAntibiotico(self, nombre_producto: str, dosis: float = None, tipo_animal: str = None, precio: float = None, cantidad: int = None):
        if self.nombre_producto == nombre_producto:
            if dosis is not None:
                self.dosis = dosis
            if tipo_animal is not None:
                self.tipo_animal = tipo_animal
            if precio is not None:
                self.precio = precio
            if cantidad is not None:
                self.cantidad = cantidad
            print(f"Antibiotico {nombre_producto} actualizado correctamente.")
        else:
            print(f"Antibiotico {nombre_producto} no encontrado.")
