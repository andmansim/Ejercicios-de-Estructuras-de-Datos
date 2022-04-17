def imprime_datos(lista):
    print('Vista de las frases que ha elegido:')
    #for i in range(len(lista)):
        #print(lista[i])

class Imprimir:
    def __init__(self, lista):
        self.lista = lista
        for i in range(len(self.lista)):
            print(self.lista[i])

