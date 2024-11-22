import sys
from PyQt5 import QtWidgets, uic
import os
from controladores.controlador_cliente import ControladorCliente

class VentanaBuscarCliente(QtWidgets.QMainWindow):
    def __init__(self, accion):
        super(VentanaBuscarCliente, self).__init__()
        self.controller = ControladorCliente()
        ui_path = os.path.join(os.path.dirname(__file__), 'ventana_buscar_cliente.ui')
        uic.loadUi(ui_path, self)
        self.pushButton_enviar.clicked.connect(self.enviar_datos)
        self.datos_cliente = []
        self.accion = accion
        print(self.accion)

    def enviar_datos(self):
        nombre = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit_nombre').toPlainText()
        dni = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit_dni').toPlainText()

        if not all([nombre, dni]):
            QtWidgets.QMessageBox.warning(self, 'Alerta', 'Por favor, complete todos los campos.')
        else:
            if self.accion == "Agregar cliente":
                if self.controller.agregar_cliente(nombre, dni):
                    QtWidgets.QMessageBox.information(self, 'Éxito', 'Cliente agregado exitosamente.')
                else:
                    QtWidgets.QMessageBox.warning(self, 'Error', f"Ya existe un cliente con DNI {dni}.")
            elif self.accion == "Modificar cliente":
                if self.controller.actualizar_cliente(dni, nombre):
                    QtWidgets.QMessageBox.information(self, 'Éxito', 'Cliente modificado exitosamente.')
                else:
                    QtWidgets.QMessageBox.warning(self, 'Error', f"No se encontró un cliente con DNI {dni}.")
            elif self.accion == "Eliminar cliente":
                if self.controller.eliminar_cliente(dni):
                    QtWidgets.QMessageBox.information(self, 'Éxito', 'Cliente eliminado exitosamente.')
                else:
                    QtWidgets.QMessageBox.warning(self, 'Error', f"No se encontró un cliente con DNI {dni}.")