import unittest


def numero_par(numero: int):
    return numero % 2 == 0
    

# los escenarios de testing estan basados en clases

class PruebaTest(unittest.TestCase):

    def test_sumatoria(self):
        numero1 = 1
        numero2 = 2
        resultado = numero1 + numero2

        self.assertEqual(resultado, 3)



    @unittest.expectedFailure
    def test_resta(self):
        numero1 = 1
        numero2 = 2
        resultado = numero1 - numero2

        self.assertEqual(resultado, 3)

class NumeroParTest(unittest.TestCase):
    def test_par(self):
        resultado = numero_par(2)
        self.assertEqual(resultado, True)

    def test_impar(self):
        resultado = numero_par(3)
        self.assertEqual(resultado, False)


    def test_error(self):
    
        with self.assertRaises(TypeError, msg='Error al ingresar un caracter en vez de un numero') as error:
             numero_par('a')

        self.assertEqual(error.msg, 'Error al ingresar un caracter en vez de un numero')







































































































