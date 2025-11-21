def Encuentra(self, lista, elemento):
        """ Recibe una lista de numeros enteros y retorna si el elemento esta en la lista"""
        for item in lista:
            if item == elemento:
                return True
        return False