from PyQt5 import QtWidgets, uic
import os
import sys

from interfaz.ventana_agregar_producto import VentanaAgregarProducto
from interfaz.ventana_modificar_producto import VentanaModificarProductos
from interfaz.ventana_buscar_producto import VentanaBuscarProducto


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ui_path = os.path.join(os.path.dirname(__file__), 'main_window_tienda.ui')
        uic.loadUi(ui_path, self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        self.pushButton_agregar_producto.clicked.connect(self.openAgregarProductoWindow)
        self.pushButton_modificar_producto.clicked.connect(self.pushButtonModificarProducto)
        self.pushButton_eliminar_producto.clicked.connect(self.pushButtonEliminarProducto)

    # Clientes

    # Productos
    def openAgregarProductoWindow(self):
        self.ventana_buscar_producto = VentanaBuscarProducto("Agregar producto")
        self.ventana_buscar_producto.show()

    def pushButtonModificarProducto(self):
        self.ventana_buscar_producto = VentanaBuscarProducto("Modificar producto")
        self.ventana_buscar_producto.show()

    def pushButtonEliminarProducto(self):
        self.ventana_buscar_producto = VentanaBuscarProducto("Eliminar producto")
        self.ventana_buscar_producto.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())