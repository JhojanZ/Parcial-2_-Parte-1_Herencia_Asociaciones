from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import uic
import sys
import os


class VentanaMostrarDatos(QMainWindow):
    def __init__(self, encabezado=[], clientes=[]):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "ventana_mostrar_datos.ui")
        uic.loadUi(ui_path, self)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(encabezado)  # Encabezados

        for cliente in clientes:
            row = []
            for head in encabezado:
                item = QStandardItem(cliente[head])
                item.setEditable(False)
                row.append(item)
            self.model.appendRow(row)
        self.mostrar_datos.setModel(self.model)
        self.mostrar_datos.resizeColumnsToContents()  
