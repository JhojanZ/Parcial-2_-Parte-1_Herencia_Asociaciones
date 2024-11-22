from PyQt5 import QtWidgets, uic
import os
import sys

from interfaz.ventana_agregar_producto import VentanaAgregarProducto


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ui_path = os.path.join(os.path.dirname(__file__), 'main_window_tienda.ui')
        uic.loadUi(ui_path, self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        self.pushButton_agregar_productos.clicked.connect(self.openAgregarProductoWindow)

    def openAgregarProductoWindow(self):
        print("Agregar producto")     
        self.ventana_agregar_producto = VentanaAgregarProducto()
        self.ventana_agregar_producto.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())