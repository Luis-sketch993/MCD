import unittest

def mcd(a, b):
    """Calcula el máximo común divisor de dos números usando el algoritmo de Euclides."""
    while b:
        a, b = b, a % b
    return abs(a)

def mcd_cuatro_numeros(a, b, c, d):
    """Calcula el máximo común divisor de cuatro números."""
    return mcd(mcd(a, b), mcd(c, d))

class TestMCD(unittest.TestCase):
    def test_mcd_dos_numeros(self):
        esperado = 6
        actual = mcd(48, 18)
        self.assertEqual(actual, esperado)

    def test_mcd_cuatro_numeros(self):
        esperado = 6
        actual = mcd_cuatro_numeros(48, 18, 30, 12)
        self.assertEqual(actual, esperado)

        esperado = 1
        actual = mcd_cuatro_numeros(7, 11, 13, 17)
        self.assertEqual(actual, esperado)

        esperado = 5
        actual = mcd_cuatro_numeros(5, 10, 15, 20)
        self.assertEqual(actual, esperado)

        esperado = 0
        actual = mcd_cuatro_numeros(0, 0, 0, 0)
        self.assertEqual(actual, esperado)

if __name__ == '__main__':
    unittest.main()
