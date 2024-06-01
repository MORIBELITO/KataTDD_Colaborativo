import unittest
from src.logica.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    def test_conjunto_vacio_retornaNone(self):
        datos = []
        pesos = []
        conjunto = Conjunto(datos, pesos)
        self.assertIsNone(conjunto.promedio())
