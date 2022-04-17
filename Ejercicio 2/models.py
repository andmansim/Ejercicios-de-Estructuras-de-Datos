class Mayusculas:
    def __init__(self, lista):
        self.lista = lista
    def mayuscula(self):
        for j in range (len(self.lista)):
            
            self.lista[j] = self.lista[j].upper()
             
        return self.lista


class Escribir:
    def __init__(self, lista):
        self.lista = lista
        self.lista_mayus = []
        f = open('frases_mayusculas.txt', 'w')
        for x in range(len(self.lista)):
            f.write(self.lista[x] + '\n')
            self.lista_mayus.append (self.lista[x])
        f.close()
    def get_lista(self):
        return self.lista_mayus 
    

