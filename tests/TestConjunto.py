import unittest
from src.logica.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([])
        resultado = conjunto.promedio()
        print(f"Test conjunto vacío: {resultado}")
        self.assertIsNone(resultado)

    def test_conjunto_unElemento_retornaValorUnicoElemento(self):
        conjunto = Conjunto([5])
        resultado = conjunto.promedio()
        print(f"Test un elemento: {resultado}")
        self.assertEqual(5, resultado)

    def test_conjunto_unElemento_conPesos_retornaValorUnicoElementoPonderado(self):
        conjunto = Conjunto([5], [3])  # Conjunto con un solo elemento y su peso
        resultado = conjunto.promedio()
        print(f"Test un elemento con peso: {resultado}")
        self.assertEqual(5, resultado)

if __name__ == "__main__":
    unittest.main()

