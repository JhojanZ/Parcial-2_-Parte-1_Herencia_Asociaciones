import unittest
from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.control_plagas import ProductoControlPlagas
from modelo.controlFertilizantes import ControlFertilizantes
from modelo.antibioticos import Antibiotico

class TestCliente(unittest.TestCase):
    def setUp(self):
        self.factura1 = Factura("17-10-2024", 0)
        self.factura2 = Factura("06-10-2024", 0)

        self.cliente = Cliente("Simon Nuñez Giraldo", "1007342001")
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

        self.assertEqual(2, len(self.cliente.factura), "Cliente no tiene facturas asociadas.")

if __name__ == '__main__':
    unittest.main()