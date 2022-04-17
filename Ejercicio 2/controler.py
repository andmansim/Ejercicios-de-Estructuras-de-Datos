from models import Mayusculas, Escribir
from view import Imprimir
lista = []
def visitante():
    
    print('Introduce una frase')
    usuario = input()
    lista.append (usuario)
    print('Introduce otra frase')
    usuario2 = input()
    lista.append (usuario2)
    
if __name__ == "__main__":
    visitante()
    lista1 = Mayusculas(lista).mayuscula()
    lista_final = Escribir(lista1)
    a = Imprimir(lista_final)
   
    
    
    
    