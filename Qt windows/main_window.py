from PyQt5 import QtWidgets, uic
import os
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ui_path = os.path.join(os.path.dirname(__file__), 'main_window_tienda.ui')
        uic.loadUi(ui_path, self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        # Setup UI components and signals here
        pass

    def openAgregarProductoWindow(self):
        self.ventana_agregar_producto.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())