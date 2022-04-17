# Ejercicios-de-Estructuras-de-Datos

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/andmansim/Ejercicios-de-Estructuras-de-Datos.git)
https://github.com/andmansim/Ejercicios-de-Estructuras-de-Datos.git

He realizado 3 ejercicios, los cules son:

# Ejercicio 1
```
class Bloque:
    def __init__(self):
        self.instrucciones = []
    
    def agregarInstruccion(self, instruccion):
        self.instrucciones.append(instruccion)

class Si:
    def __init__(self, condicion, entonces, si_no):
        self.condicion = condicion
        self.entonces = entonces
        self.si_no = si_no
    def verificar(self):
        if self.condicion :
            Mostrar(self.entonces).ver()
        else:
            Mostrar(self.si_no).ver()
            
class MientrasQue:
    def __init__(self, condicion, bloque):
        self.condicion = condicion
        self.bloque = bloque
        while self.condicion:
            Mostrar(self.bloque).ver

class Mostrar:
    def __init__(self, mensaje):
        self.mensaje = mensaje
    def ver(self):
        
        print(self.mensaje)

def visitante():
    
    mostrar_ok = Mostrar('"OK"')
    mostrar_ko = Mostrar('"KO"')

    alternativa1 = 2 + 2 == 4 
    alternativa2 = 2 + 3 == 20
    a = Si(alternativa1, mostrar_ok.mensaje, mostrar_ko.mensaje)
    a.verificar()
    b = Si(alternativa2, mostrar_ok.mensaje, mostrar_ko.mensaje)
    b.verificar()
    bloque_alternativa = Bloque()
    bloque_alternativa.agregarInstruccion(a)
    bloque_alternativa.agregarInstruccion(b)
    c = MientrasQue(True, bloque_alternativa)
    print(bloque_alternativa.instrucciones)

visitante()
```
# Ejercicio 2
```
#controler
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
    lista1 = Mayusculas(lista).mayuscula()
    lista_final = Escribir(lista1).get_lista()
    
    imprime_datos(lista_final)
   
    
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
    
#view
def imprime_datos(lista):
    print('Vista de las frases que ha elegido:')
    for i in range(len(lista)):
        print(lista[i])


```
# Ejercicio 3
```
from enum import Enum

class Producto:
    def __init__(self, tipo):
        self.tipo = tipo
        self.precio = 100
        
    def facturar(self):
        precio_final = self.precio + (self.precio * self.tipo.value)
        return precio_final

class Naturaleza(Enum):
    ALIMENTACION = 0.055
    SERVICIO = 0.2
  
class FactoryFactura:
    def crear(self, productos):
        self.producto = productos
        return self.producto
    


producto = Producto(Naturaleza.ALIMENTACION)
b = FactoryFactura()
precio_neto = b.crear(producto).facturar()
print('Precio de la alimentación: ' + str(precio_neto))

producto = Producto(Naturaleza.SERVICIO)
b = FactoryFactura()
precio_neto = b.crear(producto).facturar()
print('Precio del servicio: ' + str(precio_neto))

```
