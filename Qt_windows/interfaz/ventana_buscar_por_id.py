import sys
from PyQt5 import QtWidgets, uic
import os

class VentanaBuscarPorId(QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaBuscarPorId, self).__init__()
        ui_path = os.path.join(os.path.dirname(__file__), 'ventana_buscar_por_id.ui')
        uic.loadUi(ui_path, self)
        self.pushButton_buscar.clicked.connect(self.buscar_por_id)

    def buscar_por_id(self):
        id = self.findChild(QtWidgets.QLineEdit, 'lineEdit_id').text()
        print(f"Buscando por ID: {id}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaBuscarPorId()
    ventana.show()
    sys.exit(app.exec_())