from models import Mayusculas, Escribir
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
    Escribir(lista1)
    