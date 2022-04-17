from models import Mayusculas, Escribir
from view import imprime_datos
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
    print(lista)
    lista1 = Mayusculas(lista).mayuscula
    print(lista1)
   
    
    
    
    