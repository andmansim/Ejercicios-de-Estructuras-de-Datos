class Producto:
    def __init__(self, tipo):
        self.tipo = tipo
    def get_tipo(self):
        return self.tipo

class Naturaleza:
    def __init__(self):
        self.iva_a = 5.5/100
        self.iva_s = 20/100
    def alimentaria(self):
        return self.iva_a
    def servicio(self):
        return self.iva_s
    
class FactoryFactura:
    def __init__(self):
        self.precio = 100
    def crear(self, productos):
        self.producto = productos
        return self.producto
    def facturar(self):
        self.precio_final = self.precio + (self.precio * self.producto)
        return self.precio_final

a = Naturaleza()
producto = Producto(a.alimentaria)
print(producto)
b = FactoryFactura()
p = b.crear(producto)
precio_neto = p.facturar()
print(precio_neto)