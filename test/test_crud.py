import unittest
from modelo.cliente import Cliente
from modelo.productoControl import ProductoControl
from CRUD.crud import ClienteCrud, ProductoControlCrud

class TestCrud(unittest.TestCase):
    def setUp(self):
        self.cliente_crud = ClienteCrud()
        self.producto_crud = ProductoControlCrud()

    def test_crear_cliente(self):
        self.cliente_crud.crear_cliente("Juan Perez", 12345678)
        cliente = self.cliente_crud.leer_clientes()
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente.nombre, "Juan Perez")
        self.assertEqual(cliente.dni, 12345678)

    def test_leer_cliente(self):
        self.cliente_crud.crear_cliente("Ana Gomez", 87654321)
        clientes = self.cliente_crud.leer_clientes()
        self.assertEqual(clientes.nombre, "Ana Gomez")
        self.assertEqual(clientes.dni, 87654321)

    def test_actualizar_cliente(self):
        self.cliente_crud.crear_cliente("Carlos Ruiz", 55555555)
        self.cliente_crud.actualizar_cliente(55555555, nombre="Carlos R.")
        cliente_actualizado = self.cliente_crud.leer_clientes()
        self.assertEqual(cliente_actualizado.nombre, "Carlos R.")

    def test_eliminar_cliente(self):
        self.cliente_crud.crear_cliente("Laura Lopez", 44444444)
        self.cliente_crud.eliminar_cliente(44444444)
        cliente_eliminado = self.cliente_crud.leer_clientes()
        self.assertIsNone(cliente_eliminado)

    def test_crear_producto(self):
        self.producto_crud.crear_producto("001", "Insecticida", "Semanal", 1500, 10)
        producto = self.producto_crud.leer_productos()
        self.assertIsNotNone(producto)
        self.assertEqual(producto.registro_ica, "001")
        self.assertEqual(producto.nombre_producto, "Insecticida")
        self.assertEqual(producto.frecuencia_aplicacion, "Semanal")
        self.assertEqual(producto.valor, 1500)
        self.assertEqual(producto.cantidad, 10)

    def test_actualizar_producto(self):
        self.producto_crud.crear_producto("002", "Fungicida", "Mensual", 1200, 5)
        self.producto_crud.actualizar_producto("002", nombre_producto="Fungicida Plus", valor=1300)
        producto_actualizado = self.producto_crud.leer_productos()
        self.assertEqual(producto_actualizado.nombre_producto, "Fungicida Plus")
        self.assertEqual(producto_actualizado.valor, 1300)

    def test_eliminar_producto(self):
        self.producto_crud.crear_producto("003", "Herbicida", "Quincenal", 1000, 8)
        self.producto_crud.eliminar_producto("003")
        producto_eliminado = self.producto_crud.leer_productos()
        self.assertIsNone(producto_eliminado)

if __name__ == "__main__":
    unittest.main()    