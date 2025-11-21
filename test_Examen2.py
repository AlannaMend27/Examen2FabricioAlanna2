import unittest
from Examen2 import MiClase

class TestObtieneValencia(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada prueba para crear el objeto"""
        self.obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2"], [0.8, 0.9])
    
    def test_numero_con_todos_digitos_impares(self):
        """Verifica que cuente correctamente con todos dígitos impares (135 → 3)"""
        resultado = self.obj.ObtieneValencia(135)
        self.assertEqual(resultado, 3)
    
    def test_numero_con_todos_digitos_pares(self):
        """Verifica que retorne 0 cuando todos los dígitos son pares (246 → 0)"""
        resultado = self.obj.ObtieneValencia(246)
        self.assertEqual(resultado, 0)

class TestDivisibleTempo(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada prueba para crear el objeto"""
        self.obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2"], [0.8, 0.9])
    
    def test_numero_primo(self):
        """Verifica que un número primo solo tiene 2 divisores (1 y él mismo) (7 → [1, 7])"""
        resultado = self.obj.DivisibleTempo(7)
        self.assertEqual(resultado, [1, 7])
    
    def test_numero_uno(self):
        """Prueba caso límite: el número 1 solo es divisible por sí mismo (1 → [1])"""
        resultado = self.obj.DivisibleTempo(1)
        self.assertEqual(resultado, [1])

class TestObtieneMasBailable(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada prueba para crear el objeto"""
        self.obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2"], [0.8, 0.9])
    
    def test_lista_vacia(self):
        """Verifica que retorna None con una lista vacía ([] → None)"""
        resultado = self.obj.ObtieneMasBailable([])
        self.assertIsNone(resultado)
    
    def test_lista_un_elemento(self):
        """Prueba caso límite: lista con un único elemento (5 → 5)"""
        resultado = self.obj.ObtieneMasBailable([5])
        self.assertEqual(resultado, 5)

class TestVerificaListaCanciones(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada prueba para crear el objeto"""
        self.obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2"], [0.8, 0.9])
    
    def test_lista_vacia(self):
        """Verifica que retorna True con una lista vacía ([] → True)"""
        resultado = self.obj.VerificaListaCanciones([])
        self.assertTrue(resultado)
    
    def test_lista_sin_valores_nulos(self):
        """Prueba lista con canciones válidas (["Song1", "Song2", "Song3"] → True)"""
        resultado = self.obj.VerificaListaCanciones(["Song1", "Song2", "Song3"])
        self.assertTrue(resultado)
        
if __name__ == '__main__':
    unittest.main()