class Mayusculas:
    def __init__(self, lista):
        self.lista = lista
    def mayuscula(self):
        for j in range (len(self.lista)):
            
            self.lista[j] = self.lista[j].upper()
        return self.lista

a = Mayusculas(['hola', 'jnfj'])
b = a.mayuscula()
class Escribir:
    def __init__(self, lista):
        f = open('frases_mayusculas.txt', 'a')
        for x in range(len(lista)):
            f.write(lista[x] + '\n')
        f.close()
    
e = Escribir(b)
