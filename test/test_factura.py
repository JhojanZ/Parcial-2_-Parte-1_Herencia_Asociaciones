import unittest

from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.control_plagas import ProductoControlPlagas
from modelo.controlFertilizantes import ControlFertilizantes
from modelo.antibioticos import Antibiotico

class TestFactura(unittest.TestCase):
    def setUp(self):
        self.fact = Factura("31-12-2023", 0)

        self.cliente = Cliente("Simon Nuñez Giraldo", "1007342001")
        self.produc_plaga = ProductoControlPlagas("ABC10", "Plaga X", "20", 30000, 1, "30" )
        self.produc_fertilizante = ControlFertilizantes("QWE20", "Fertilizante Y", "20", 20000, 2, "31-12-2024")
        self.antibio_1 = Antibiotico("Antibiotico x", "400", "Porcino", 20000, 1)
        self.antibio_2 = Antibiotico("Antibiotico y", "600", "Bovino", 30000, 1)
    
    def test_vende_varios_productos_control(self):
        self.fact.asociar_producto_control(self.produc_fertilizante)
        self.fact.asociar_producto_control(self.produc_plaga)

        self.assertEqual(2, len(self.fact.producto_control), "No se han asociado productos de control.")

    def test_vende_varios_antibiotico(self):
        self.fact.asociar_antibiotico(self.antibio_1)
        self.fact.asociar_antibiotico(self.antibio_2)

        self.assertEqual(2, len(self.fact.antibiotico), "No se han asociado antibioticos.")

    def test_vende_varios_antibioticos_productos_control(self):
        self.fact.asociar_producto_control(self.produc_fertilizante)
        self.fact.asociar_producto_control(self.produc_plaga)
        self.fact.asociar_antibiotico(self.antibio_1)
        self.fact.asociar_antibiotico(self.antibio_2)

        self.assertEqual(2, len(self.fact.producto_control), "No se han asociado productos de control.")
        self.assertEqual(2, len(self.fact.antibiotico), "No se han asociado antibioticos.")

    def test_realizar_venta_productos(self):
        self.fact.realizar_venta(self.produc_fertilizante)

        #falta