class Mayusculas:
    def __init__(self, lista):
        self.lista = lista
    def mayuscula(self):
        for j in range (len(self.lista)):
            
            self.lista[j] = self.lista[j].upper()
        print(self.lista)

a = Mayusculas(['hola', 'jnfj'])
a.mayuscula()
