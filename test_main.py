import unittest
from main import suma

class TestSuma(unittest.TestCase):
    def test_suma_positiva(self):
        self.assertEqual(suma(2, 3), 5)

    def test_suma_negativa(self):
        self.assertEqual(suma(-1, -1), -2)

class TestResta(unittest.TestCase):
    def test_resta_positiva(self):
        self.assertEqual(resta(3, 1), 2)

    def test_resta_negativa(self):
        self.assertEqual(resta(-2, -2), 0)

if __name__ == '__main__':
    unittest.main()
