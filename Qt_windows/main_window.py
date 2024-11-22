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
        self.controlador_cliente = ControladorCliente()
        self.controlador_ventanas = ControladorVentanas(self)

    def setupUi(self, MainWindow):
        self.pushButton_agregar_cliente.clicked.connect(self.pushAgregarCliente)
        self.pushButton_agregar_producto.clicked.connect(self.pushAgregarProducto)

        

        self.pushButton_mostrar_lista_clientes.clicked.connect(self.pushButtonMostrarClientes)
        self.pushButton_mostrar_lista_productos.clicked.connect(self.pushButtonMostrarProductos)
        self.pushButton_mostrar_facturas.clicked.connect(self.pushButtonMostrarFactura)

        
        """
        self.pushButton_agregar_producto.clicked.connect(self.openAgregarProductoWindow)
        self.pushButton_modificar_producto.clicked.connect(self.pushButtonModificarProducto)
        self.pushButton_eliminar_producto.clicked.connect(self.pushButtonEliminarProducto)

        self.pushButton_agregar_cliente.clicked.connect(self.pushAgregarCliente)
        self.pushButton_modificar_cliente.clicked.connect(self.pushModificarCliente)
        self.pushButton_eliminar_cliente.clicked.connect(self.pushEliminarCliente)

        self.pushButton_mostrar_lista_clientes.clicked.connect(self.pushButtonMostrarClientes)
        self.pushButton_mostrar_lista_productos.clicked.connect(self.pushButtonMostrarProductos)

        self.pushButton_crear_factura.clicked.connect(self.pushButtonCrearFactura)
        self.pushButton_mostrar_facturas.clicked.connect(self.pushButtonMostrarFactura)
        """

    # Clientes
    def pushAgregarCliente(self):
        accion = "Agregar cliente"
        self.controlador_ventanas.abrir_ventana_buscar_cliente(accion)

    # Productos
    def pushAgregarProducto(self):
        accion = "Agregar producto"
        self.controlador_ventanas.abrir_ventana_buscar_producto(accion)


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
"""
    # Clientes
    def pushAgregarCliente(self):
        self.ventana_buscar_cliente = VentanaBuscarCliente("Agregar cliente")
        self.ventana_buscar_cliente.show()


    def pushModificarCliente(self):
        self.ventana_buscar_cliente = VentanaBuscarCliente("Modificar cliente")
        self.ventana_buscar_cliente.show()

    def pushEliminarCliente(self): 
        self.ventana_buscar_cliente = VentanaBuscarCliente("Eliminar cliente")
        self.ventana_buscar_cliente.show()
        

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

    # Mostrar tipo
    def pushButtonMostrarClientes(self):
        cabezera = ["Nombre", "DNI"]
        clientes = self.controlador_cliente.obtener_clientes()
        clientes.append(["jjjjj", "123"]) #testig

 
        self.ventana_mostrar_datos = VentanaMostrarDatos(cabezera, clientes)
        self.ventana_mostrar_datos.show()

    def pushButtonMostrarProductos(self):
        cabezera = [] #implementar funcion para obtener los encabezados
        productos = [] #implementar funcion para obtener los productos
        self.ventana_mostrar_datos = VentanaMostrarDatos(cabezera, productos)
        self.ventana_mostrar_datos.show()

    # Factura
    def pushButtonCrearFactura(self):
        self.ventana_buscar_cliente = VentanaBuscarCliente("Crear factura")
        self.ventana_buscar_cliente.show()

    def pushButtonMostrarFactura(self):
        cabezera = [] #implementar funcion para obtener los encabezados
        facturas = [] #implementar funcion para obtener las facturas
        self.ventana_mostrar_datos = VentanaMostrarDatos(cabezera, facturas)
        self.ventana_mostrar_datos.show()

        """
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())