class Mayusculas:
    def __init__(self, lista):
        self.lista = lista
    def mayuscula(self):
        for j in range (len(self.lista)):
            
            self.lista[j] = self.lista[j].upper()
        return self.lista


class Escribir:
    def __init__(self, lista):
        f = open('frases_mayusculas.txt', 'w')
        for x in range(len(lista)):
            f.write(lista[x] + '\n')
        f.close()
    

