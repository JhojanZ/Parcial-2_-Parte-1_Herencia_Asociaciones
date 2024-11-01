import unittest
from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.control_plagas import ProductoControlPlagas
from modelo.controlFertilizantes import ControlFertilizantes
from modelo.antibioticos import Antibiotico

class TestCliente(unittest.TestCase):
    CLIENTE_NOMBRE = "Simon Nuñez Giraldo"
    CLIENTE_DNI = "1007342001"

    def setUp(self):
        self.factura1 = Factura("17-10-2024", 0)
        self.factura2 = Factura("06-10-2024", 0)      

        self.cliente = Cliente(self.CLIENTE_NOMBRE, self.CLIENTE_DNI)
        self.produc_plaga = ProductoControlPlagas("ABC10", "Plaga X", "20", 30000, 1, "30" )
        self.produc_fertilizante = ControlFertilizantes("QWE20", "Fertilizante Y", "20", 20000, 2, "31-12-2024")
        self.antibio_1 = Antibiotico("Antibiotico x", "400", "Porcino", 20000, 1)
        self.antibio_2 = Antibiotico("Antibiotico y", "600", "Bovino", 30000, 1)

    def test_cliente_tiene_varias_facturas(self):
        self.factura1.asociar_antibiotico(self.antibio_1)
        self.factura1.asociar_antibiotico(self.antibio_2)
        self.factura1.asociar_producto_control(self.produc_plaga)
        self.factura1.asociar_producto_control(self.produc_fertilizante)

        self.factura2.asociar_antibiotico(self.antibio_1)
        self.factura2.asociar_antibiotico(self.antibio_2)
        self.factura2.asociar_producto_control(self.produc_plaga)
        self.factura2.asociar_producto_control(self.produc_fertilizante)

        self.cliente.agregar_factura(self.factura1)
        self.cliente.agregar_factura(self.factura2)
        numero_facturas = 2

        self.assertEqual(len(self.cliente.factura),  numero_facturas, "Cliente no tiene facturas asociadas.")

    def test_get_nombre(self):
        self.assertEqual(self.cliente.nombre, self.CLIENTE_NOMBRE, "El nombre del cliente no es el esperado.")

    def test_set_nombre(self):
        nuevo_nombre = "Laura Ramirez"
        self.cliente.nombre = nuevo_nombre
        self.assertEqual(self.cliente.nombre, nuevo_nombre, "No se actualizó correctamente el nombre del cliente.")

    def test_get_dni(self):
        self.assertEqual(self.cliente.dni, self.CLIENTE_DNI, "El DNI del cliente no es el esperado.")

    def test_set_dni(self):
        nuevo_dni = "1007342002"
        self.cliente.dni = nuevo_dni
        self.assertEqual(self.cliente.dni, nuevo_dni, "El DNI del cliente no se actualizó correctamente.")

    def test_agregar_factura(self):
        self.cliente.agregar_factura(self.factura1)
        self.assertIn(self.factura1, self.cliente.factura, "La factura no se agregó correctamente.")


 

if __name__ == '__main__':
    unittest.main()