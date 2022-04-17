from models import Mayusculas, Escribir
from view import imprime_datos
lista = []
def visitante():
    
    print('Introduce una frase')
    usuario = input()
    lista.append (usuario)
    print('Introduce otra frase')
    usuarioq = input()
    lista.append (usuarioq)
    
if __name__ == "__main__":
    visitante()
    lista1 = Mayusculas(lista).mayuscula
    lista_final = Escribir(lista).get_lista()
    imprime_datos (lista_final)
    
    
    
    