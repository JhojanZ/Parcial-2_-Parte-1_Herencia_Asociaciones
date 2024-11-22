from PyQt5 import QtWidgets
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Qt_windows.interfaz.ventana_buscar_cliente import VentanaBuscarCliente
from Qt_windows.interfaz.ventana_buscar_producto import VentanaBuscarProducto
from Qt_windows.interfaz.ventana_mostrar_datos import VentanaMostrarDatos

from controladores.controlador_cliente import ControladorCliente
from controladores.controlador_productos import ControladorProductos


class ControladorVentanas:
    def __init__(self, main_window):
        self.main_window = main_window
        self.controlador_cliente = ControladorCliente(main_window)
        self.controlador_productos = ControladorProductos(main_window)
        self.ventana_buscar_producto = None

    def mostrar_main_window(self):
        self.main_window.show()

    def abrir_ventana_buscar_cliente(self, accion):
        print("abrir_ventana_buscar_cliente")
        print(accion)
        print(type(accion))
        self.ventana_buscar_cliente = VentanaBuscarCliente(accion, self.controlador_cliente)
        self.ventana_buscar_cliente.show()

    def abrir_ventana_buscar_producto(self, accion):
        self.ventana_buscar_producto = VentanaBuscarProducto(accion)
        self.ventana_buscar_producto.show()

    # mostrar datos
    def abrir_ventana_mostrar_datos(self, tipo):
        datos = self.enviar_informacion(tipo)
        print(datos)
        self.ventana_mostrar_datos = VentanaMostrarDatos(datos[0], datos[1])
        self.ventana_mostrar_datos.show()

    def enviar_informacion(self, tipo):
        if(tipo == "clientes"):
            return self.convertir_lista_objetos_a_lista_diccionarios(self.controlador_cliente.obtener_clientes())
        elif(tipo == "productos"):
            return self.convertir_lista_objetos_a_lista_diccionarios(self.controlador_productos.obtener_productos())
        elif(tipo == "facturas"):
            #return self.convertir_lista_objetos_a_lista_diccionarios(self.controlador_factura.obtener_facturas())
            pass
        else:
            return [[], []]


    def convertir_lista_objetos_a_lista_diccionarios(self, lista_objetos):
        lista_diccionarios = []
        header = []

        if(len(lista_objetos) == 0):
            return [[], []]
        
        for key in lista_objetos[0].__dict__.keys():
            header.append(key)

        for objeto in lista_objetos:
            lista_diccionarios.append(objeto.__dict__)
        return [header, lista_diccionarios]

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sys.exit(app.exec_())