import sys
from PyQt5 import QtWidgets, uic
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from controladores.controlador_cliente import ControladorCliente

class VentanaFactura(QtWidgets.QMainWindow):
    def __init__(self, controlador_cliente):
        super(VentanaFactura, self).__init__()
        self.controlador = controlador_cliente
        ui_path = os.path.join(os.path.dirname(__file__), 'ventana_factura.ui')
        uic.loadUi(ui_path, self)    
        self.pushButton_enviar.clicked.connect(self.enviar_datos)
        print(f"Loading UI from: {ui_path}")


    def enviar_datos(self):

        # Obtener valores de los campos de texto
        dni = self.findChild(QtWidgets.QLineEdit, 'lineEdit_dni').text()
        fecha = self.findChild(QtWidgets.QLineEdit, 'lineEdit').text()
        cantidad = self.findChild(QtWidgets.QLineEdit, 'lineEdit_3').text()
        valor_total = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2').text()

        # Obtener producto del QComboBox
        producto_combo = self.findChild(QtWidgets.QComboBox, 'comboBox')
        producto_seleccionado = producto_combo.currentText()  # Texto del elemento seleccionado

        if not all([dni, cantidad, valor_total, producto_seleccionado]):
            QtWidgets.QMessageBox.warning(self, 'Alerta', 'Por favor, complete todos los campos.')
        else:
            if self.controller.agregar_factura(dni, fecha, cantidad, producto_seleccionado):
                    QtWidgets.QMessageBox.information(self, 'Éxito', 'Factura agregada exitosamente.')
                