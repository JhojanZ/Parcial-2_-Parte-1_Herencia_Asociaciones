
class Antibiotico:
    def __init__(self, nombre_antibiotico, dosis, tipo_animal, valor, cantidad):
        self.__nombre_antibiotico = nombre_antibiotico
        self.__dosis = dosis
        self.__tipo_animal = tipo_animal
        self.__valor = valor
        self.__cantidad = cantidad

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
        return self.__valor
    
    @precio.setter
    def precio(self, precio):
        self.__valor = precio
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

