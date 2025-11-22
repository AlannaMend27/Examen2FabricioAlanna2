import unittest
from Examen2 import MiClase

class TestObtieneValencia(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada prueba para crear el objeto"""
        self.obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2"], [0.8, 0.9])
    
    def test_numero_con_todos_digitos_impares(self):
        """Verifica que cuente correctamente con todos dígitos impares"""
        resultado = self.obj.ObtieneValencia(135)
        self.assertEqual(resultado, 3)
    
    def test_numero_con_todos_digitos_pares(self):
        """Verifica que retorne 0 cuando todos los dígitos son pares"""
        resultado = self.obj.ObtieneValencia(246)
        self.assertEqual(resultado, 0)

    def test_numero_con_digitos_mixtos(self):
        """Prueba un número con dígitos pares e impares"""
        resultado = self.obj.ObtieneValencia(12345)
        self.assertEqual(resultado, 3)
    
    def test_numero_de_un_digito_impar(self):
        """Prueba un número de un solo dígito impar"""
        resultado = self.obj.ObtieneValencia(7)
        self.assertEqual(resultado, 1)


class TestDivisibleTempo(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada prueba para crear el objeto"""
        self.obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2"], [0.8, 0.9])
    
    def test_numero_primo(self):
        """Verifica que un número primo solo tiene 2 divisores"""
        resultado = self.obj.DivisibleTempo(7)
        self.assertEqual(resultado, [1, 7])
    
    def test_numero_uno(self):
        """Prueba caso límite: el número 1 solo es divisible por sí mismo"""
        resultado = self.obj.DivisibleTempo(1)
        self.assertEqual(resultado, [1])

    def test_numero_con_multiples_divisores(self):
        """Verifica que encuentra todos los divisores correctamente"""
        resultado = self.obj.DivisibleTempo(12)
        self.assertEqual(resultado, [1, 2, 3, 4, 6, 12])
    
    def test_numero_potencia_de_dos(self):
        """Prueba un número potencia de dos"""
        resultado = self.obj.DivisibleTempo(8)
        self.assertEqual(resultado, [1, 2, 4, 8])


class TestObtieneMasBailable(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada prueba para crear el objeto"""
        self.obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2"], [0.8, 0.9])
    
    def test_lista_vacia(self):
        """Verifica que retorna None con una lista vacía"""
        resultado = self.obj.ObtieneMasBailable([])
        self.assertIsNone(resultado)
    
    def test_lista_un_elemento(self):
        """Prueba caso límite: lista con un único elemento"""
        resultado = self.obj.ObtieneMasBailable([5])
        self.assertEqual(resultado, 5)

    # esta es la prueba modificada para que falle (Punto 3 parte III examen)
    def test_lista_desordenada(self):
        """Verifica que encuentra el mayor en lista desordenada"""
        resultado = self.obj.ObtieneMasBailable([3, 9, 1, 7, 2])
        self.assertEqual(resultado, 7)
    
    def test_lista_con_numeros_negativos(self):
        """Prueba con números negativos"""
        resultado = self.obj.ObtieneMasBailable([-5, -2, -10, -1])
        self.assertEqual(resultado, -1)


class TestVerificaListaCanciones(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada prueba para crear el objeto"""
        self.obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2"], [0.8, 0.9])
    
    def test_lista_vacia(self):
        """Verifica que retorna True con una lista vacía"""
        resultado = self.obj.VerificaListaCanciones([])
        self.assertTrue(resultado)
    
    def test_lista_sin_valores_nulos(self):
        """Prueba lista con canciones válidas"""
        resultado = self.obj.VerificaListaCanciones(["Song1", "Song2", "Song3"])
        self.assertTrue(resultado)

    def test_lista_con_un_valor_nulo(self):
        """Verifica que retorna False cuando hay un None en la lista"""
        resultado = self.obj.VerificaListaCanciones(["Song1", None, "Song3"])
        self.assertFalse(resultado)
    
    def test_lista_solo_con_nulos(self):
        """Prueba lista con solo valores None"""
        resultado = self.obj.VerificaListaCanciones([None, None])
        self.assertFalse(resultado)

class TestEncuentra(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada prueba para crear el objeto"""
        self.obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2"], [0.8, 0.9])
    
    def test_encuentra_true(self):
        """Verifica que el método Encuentra retorna True cuando el elemento está en la lista"""
        resultado = self.obj.Encuentra([1, 2, 3, 4, 5], 3)
        self.assertTrue(resultado)
    
    def test_encuentra_false(self):
        """Verifica que el método Encuentra retorna False cuando el elemento no está en la lista"""
        resultado = self.obj.Encuentra([1, 2, 3, 4, 5], 10)
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()