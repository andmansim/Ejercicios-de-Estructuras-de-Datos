# models
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
    def get_lista(self):
        lista_mayus = []
        f = open('frases_mayusculas.txt', 'w')
        for x in range(len(self.lista)):
            f.write(self.lista[x] + '\n')
            lista_mayus.append(self.lista[x])
        f.close()
        return lista_mayus
    
