import sys
from PyQt5 import QtWidgets, uic
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from controladores.controlador_productos import ControladorProductos


class VentanaBuscarProducto(QtWidgets.QMainWindow):
    def __init__(self, accion, controlador_producto):
        super(VentanaBuscarProducto, self).__init__()
        ui_path = os.path.join(os.path.dirname(__file__), 'ventana_agregar_producto.ui')
        uic.loadUi(ui_path, self)
        self.controlador_producto = controlador_producto
        self.pushButton_enviar.clicked.connect(self.enviar_datos)
        self.datos_producto = []
        self.accion = accion
        print(self.accion)

    def enviar_datos(self):
        nombre = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit_nombre').toPlainText()
        registro_ica = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit_registro_ica').toPlainText()
        frecuencia_aplicacion = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit_frecuencia_aplicacion').toPlainText()
        valor_producto = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit_valor_producto').toPlainText()
        cantidad = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit_cantidad').toPlainText()

        # Validacion de que los campos sean numericos
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
            datos = {
                'registro_ica': registro_ica,
                'nombre_producto': nombre,
                'frecuencia_aplicacion': frecuencia_aplicacion,
                'valor': valor_producto,
                'cantidad': cantidad
            }
            self.controlador_producto.agregar_producto(**datos)

            

"""
            if self.accion == "Agregar producto":
                if self.controller_producto.agregar_producto(nombre, registro_ica, frecuencia_aplicacion, valor_producto, cantidad):
                    QtWidgets.QMessageBox.information(self, 'Éxito', 'Producto agregado exitosamente.')
                else:
                    QtWidgets.QMessageBox.warning(self, 'Error', f"Ya existe un producto con registro ICA {registro_ica}.")
            elif self.accion == "Modificar cliente":
                if self.controller_producto.actualizar_producto(registro_ica, nombre, valor_producto, cantidad):
                    QtWidgets.QMessageBox.information(self, 'Éxito', 'Cliente modificado exitosamente.')
                else:
                    QtWidgets.QMessageBox.warning(self, 'Error', f"No se encontró un producto con registro ICA {registro_ica}.")
            elif self.accion == "Eliminar cliente":
                if self.controller_producto.eliminar_producto(registro_ica):
                    QtWidgets.QMessageBox.information(self, 'Éxito', 'Cliente eliminado exitosamente.')
                else:
                    QtWidgets.QMessageBox.warning(self, 'Error', f"No se encontró un producto con registro ICA {registro_ica}.")
""" 