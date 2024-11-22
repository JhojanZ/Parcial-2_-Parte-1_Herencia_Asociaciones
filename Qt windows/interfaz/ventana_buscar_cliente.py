import sys
from PyQt5 import QtWidgets, uic
import os

class VentanaBuscarCliente(QtWidgets.QMainWindow):
    def __init__(self, accion):
        super(VentanaBuscarCliente, self).__init__()
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
            self.datos_cliente.append({
                'nombre': nombre,
                'dni': dni,
                'accion': self.accion
            })
            QtWidgets.QMessageBox.information(self, 'Éxito', 'Datos guardados exitosamente.')