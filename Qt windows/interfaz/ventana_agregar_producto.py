import sys
from PyQt5 import QtWidgets, uic
import os

class VentanaAgregarProducto(QtWidgets.QMainWindow):
    def __init__(self):
        print("Ventana agregar producto")
        super(VentanaAgregarProducto, self).__init__()
        ui_path = os.path.join(os.path.dirname(__file__), 'ventana_agregar_producto.ui')
        uic.loadUi(ui_path, self)
        self.pushButton_enviar.clicked.connect(self.enviar_datos)
        self.datos_producto = []

    def enviar_datos(self):
        nombre = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit_nombre').toPlainText()
        registro_ica = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit_registro_ica').toPlainText()
        frecuencia_aplicacion = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit_frecuencia_aplicacion').toPlainText()
        valor_producto = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit_valor_producto').toPlainText()
        cantidad = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit_cantidad').toPlainText()

        # Validate if frecuencia_aplicacion, valor_producto, and cantidad are valid floats
        try:
            frecuencia_aplicacion = float(frecuencia_aplicacion)
            valor_producto = float(valor_producto)
            cantidad = float(cantidad)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, 'Alerta', 'Frecuencia de aplicación, valor del producto y cantidad deben ser valores numéricos válidos.')
            return

        if not all([nombre, registro_ica, frecuencia_aplicacion, valor_producto, cantidad]):
            QtWidgets.QMessageBox.warning(self, 'Alerta', 'Por favor, complete todos los campos.')
        else:
            self.datos_producto.append({
                'nombre': nombre,
                'registro_ica': registro_ica,
                'frecuencia_aplicacion': frecuencia_aplicacion,
                'valor_producto': valor_producto,
                'cantidad': cantidad
            })
            QtWidgets.QMessageBox.information(self, 'Éxito', 'Datos guardados exitosamente.')