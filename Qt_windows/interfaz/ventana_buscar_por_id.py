import sys
from PyQt5 import QtWidgets, uic
import os

from controladores.controlador_cliente import ControladorCliente
from controladores.controlador_productos import ControladorProductos

class VentanaBuscarPorId(QtWidgets.QMainWindow):
    def __init__(self, dato, controlador_productos, controlador_cliente):
        super(VentanaBuscarPorId, self).__init__()
        ui_path = os.path.join(os.path.dirname(__file__), 'ventana_buscar_por_id.ui')
        uic.loadUi(ui_path, self)
    

        self.controlador_productos = controlador_productos
        self.controlador_cliente = controlador_cliente

        self.pushButton_buscar.clicked.connect(self.buscar_por_id)
        self.label_inicio = self.findChild(QtWidgets.QLabel, 'label_inicio')
        self.accion = dato[0]
        self.tipo = dato[1]
        self.actualizar_mensaje()

    def actualizar_mensaje(self):
        if self.tipo == "cliente":
            self.label_inicio.setText("Ingrese el ID del cliente:")
        elif self.tipo == "producto":
            self.label_inicio.setText("Ingrese el ICA del producto:") 
        else:
            self.label_inicio.setText("Ingrese el ID:")

    def buscar_por_id(self):
        id = self.findChild(QtWidgets.QLineEdit, 'lineEdit_id').text()
        print(f"Buscando por ID: {id}")
        if self.tipo == "cliente":
            cliente = self.controlador_cliente.buscar_cliente(id, self.accion)
            print(cliente)
        elif self.tipo == "producto":
            producto = self.controlador_productos.buscar_producto(id, self.accion)
            print(producto)



