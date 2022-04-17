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
