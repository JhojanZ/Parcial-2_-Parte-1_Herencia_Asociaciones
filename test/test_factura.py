import unittest

from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.control_plagas import ProductoControlPlagas
from modelo.controlFertilizantes import ControlFertilizantes
from modelo.antibioticos import Antibiotico

class TestFactura(unittest.TestCase):
    FACTURA_FECHA = "31-12-2023"
    FACTURA_VALOR = 10

    def setUp(self):
        self.fact = Factura(self.FACTURA_FECHA, self.FACTURA_VALOR)

        self.cliente = Cliente("Simon Nuñez Giraldo", "1007342001")
        self.produc_plaga = ProductoControlPlagas("ABC10", "Plaga X", "20", 30000, 1, "30" )
        self.produc_fertilizante = ControlFertilizantes("QWE20", "Fertilizante Y", "20", 20000, 2, "31-12-2024")
        self.antibio_1 = Antibiotico("Antibiotico x", "400", "Porcino", 20000, 1)
        self.antibio_2 = Antibiotico("Antibiotico y", "600", "Bovino", 30000, 1)
    
    def test_vende_varios_productos_control(self):
        self.fact.asociar_producto_control(self.produc_fertilizante)
        self.fact.asociar_producto_control(self.produc_plaga)
        cantidad_productos = 2

        self.assertEqual(len(self.fact.producto_control), cantidad_productos, "No se han asociado productos de control.")

    def test_vende_varios_antibiotico(self):
        self.fact.asociar_antibiotico(self.antibio_1)
        self.fact.asociar_antibiotico(self.antibio_2)
        cantidad_antibioticos = 2

        self.assertEqual(len(self.fact.antibiotico), cantidad_antibioticos, "No se han asociado antibioticos.")

    def test_vende_varios_antibioticos_productos_control(self):
        self.fact.asociar_producto_control(self.produc_fertilizante)
        self.fact.asociar_producto_control(self.produc_plaga)
        self.fact.asociar_antibiotico(self.antibio_1)
        self.fact.asociar_antibiotico(self.antibio_2)

        self.assertEqual(2, len(self.fact.producto_control), "No se han asociado productos de control.")
        self.assertEqual(2, len(self.fact.antibiotico), "No se han asociado antibioticos.")

    def test_realizar_venta_productos(self):
        self.fact.realizar_venta(self.produc_fertilizante)

    def test_get_fecha(self):
        self.assertEqual(self.fact.fecha, self.FACTURA_FECHA, "La fecha inicial no es correcta.")

    def test_nueva_fecha(self):
        nueva_fecha = "01-01-2024"
        self.fact.fecha = nueva_fecha
        self.assertEqual(self.fact.fecha, nueva_fecha, "La fecha no se actualizó correctamente.")

    def test_get_valor(self):
        self.assertEqual(self.fact.valor_total_compra, self.FACTURA_VALOR, "La fecha inicial no es correcta.")

    def test_nuevo_valor(self):
        nuevo_valor = 40
        self.fact.fecha = nuevo_valor
        self.assertEqual(self.fact.fecha, nuevo_valor, "El valor no se actualizó correctamente.")

    def test_actualizar_valor_producto(self):
        nuevo_valor = 20000
        self.fact.realizar_venta(self.produc_fertilizante)
        self.assertEqual(self.fact.valor_total_compra, nuevo_valor, "El valor total no es correcto para el fertilizante.")
        
    #Este caso esta fallando
    def test_actualizar_valor_antibiotico(self):
        nuevo_valor = 20000
        self.fact.realizar_venta(antibiotico=self.antibio_1)
        self.assertEqual(self.fact.valor_total_compra, nuevo_valor, "El valor total no es correcto después de agregar un antibiótico.")