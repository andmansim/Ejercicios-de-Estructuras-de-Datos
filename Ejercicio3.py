class Producto:
    def __init__(self, tipo):
        self.tipo = tipo
    

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
        pass
    def crear(self):
        pasa el producto
    
    def facturar():
        pass
    