import sys
from PyQt5 import QtWidgets, uic
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from controladores.controlador_cliente import ControladorCliente

class VentanaBuscarCliente(QtWidgets.QMainWindow):
    def __init__(self, accion, controlador_cliente):
        super(VentanaBuscarCliente, self).__init__()
        self.controller = controlador_cliente
        self.main = controlador_cliente
        ui_path = os.path.join(os.path.dirname(__file__), 'ventana_buscar_cliente.ui')
        uic.loadUi(ui_path, self)
        self.pushButton_enviar.clicked.connect(self.enviar_datos)
        self.accion = accion
        print(f"Loading UI from: {ui_path}")


    def enviar_datos(self):
        print(self.accion)

        nombre = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit_nombre').toPlainText()
        dni = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit_dni').toPlainText()
        print(self.accion, "paso linea")

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