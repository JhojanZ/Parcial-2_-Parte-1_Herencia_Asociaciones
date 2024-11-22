from PyQt5 import QtWidgets, uic
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controladores.controlador_cliente import ControladorCliente
from controladores.contralador_ventanas import ControladorVentanas


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ui_path = os.path.join(os.path.dirname(__file__), 'main_window_tienda.ui')
        uic.loadUi(ui_path, self)
        self.setupUi(self)
        self.controlador_ventanas = ControladorVentanas(self)

    def setupUi(self, MainWindow):
        self.pushButton_agregar_cliente.clicked.connect(self.pushAgregarCliente)
        self.pushButton_agregar_producto.clicked.connect(self.pushAgregarProducto)

        self.pushButton_eliminar_cliente.clicked.connect(self.pushEliminarCliente)
        self.pushButton_modificar_cliente.clicked.connect(self.pushModificarCliente)

        self.pushButton_eliminar_producto.clicked.connect(self.pusEliminarProducto)
        self.pushButton_modificar_producto.clicked.connect(self.pushModificarProducto)

        self.pushButton_mostrar_lista_clientes.clicked.connect(self.pushButtonMostrarClientes)
        self.pushButton_mostrar_lista_productos.clicked.connect(self.pushButtonMostrarProductos)
        self.pushButton_mostrar_facturas.clicked.connect(self.pushButtonMostrarFactura)


    # Clientes
    def pushAgregarCliente(self):
        accion = "Agregar cliente"
        self.controlador_ventanas.abrir_ventana_buscar_cliente(accion)

    def pushModificarCliente(self):
        accion = ["Modificar", "cliente"]
        self.controlador_ventanas.abrir_ventana_buscar_id(accion)

    def pushEliminarCliente(self):
        accion = ["Eliminar", "cliente"]
        self.controlador_ventanas.abrir_ventana_buscar_id(accion)

    # Productos
    def pushAgregarProducto(self):
        accion = "Agregar producto"
        self.controlador_ventanas.abrir_ventana_buscar_producto(accion)

    def pushModificarProducto(self):
        accion = ["Modificar", "producto"]
        self.controlador_ventanas.abrir_ventana_buscar_id(accion)

    def pusEliminarProducto(self):
        accion = ["Eliminar", "producto"]
        self.controlador_ventanas.abrir_ventana_buscar_id(accion)

    # Facturas
    def pushAgregarFactura(self):
        pass

    def pushModificarFactura(self):
        pass

    # Mostrar datos
    def pushButtonMostrarClientes(self):
        tipo = "clientes"
        self.controlador_ventanas.abrir_ventana_mostrar_datos(tipo)

    def pushButtonMostrarProductos(self):
        tipo = "productos"
        self.controlador_ventanas.abrir_ventana_mostrar_datos(tipo)

    def pushButtonMostrarFactura(self):
        tipo = "facturas"
        self.controlador_ventanas.abrir_ventana_mostrar_datos(tipo)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())