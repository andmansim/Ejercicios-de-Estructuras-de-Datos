class Producto:
    def __init__(self, tipo):
        self.tipo = tipo
        self.precio = 100
        
    def facturar(self):
        precio_final = self.precio + (self.precio * self.tipo)
        return precio_final

class Naturaleza:
    ALIMENTACION = 5.5/100
    SERVICIO = 20/100
    def __init__(self):
        self.iva_a = 5.5/100
        self.iva_s = 20/100
    def alimentaria(self):
        return self.iva_a
    def servicio(self):
        return self.iva_s
    
class FactoryFactura:
    def crear(self, productos):
        self.producto = productos
        return self.producto
    

a = Naturaleza()
producto = Producto(a.alimentaria)
print(producto)
b = FactoryFactura()

precio_neto = b.crear(producto).facturar()
print(precio_neto)