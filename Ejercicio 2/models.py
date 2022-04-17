class Mayusculas:
    def __init__(self, lista):
        self.lista = lista
        
    def mayuscula(self):
        lista1 = []
        for j in range (len(self.lista)):
            
            self.lista[j] = self.lista[j].upper()
            print (self.lista[j].upper())
        return lista1
a = Mayusculas(['djnjdnf', 'dndf'])
b = a.mayuscula()


class Escribir:
    def __init__(self, lista):
        self.lista = lista
        lista_mayus = []
        f = open('frases_mayusculas.txt', 'w')
        for x in range(len(self.lista)):
            f.write(self.lista[x] + '\n')
            lista_mayus.append (self.lista[x])
        f.close()
       
    
c = Escribir(b)
