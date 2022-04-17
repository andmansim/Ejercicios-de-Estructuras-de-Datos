class Bloque:
    def __init__(self):
        self.instrucciones = []
    
    def agregarInstruction(self, instruccion):
        self.instrucciones.append(instruccion)

class Si:
    def __init__(self, condicion, entonces, si_no):
        self.condicion = condicion
        self.entonces = entonces
        self.si_no = si_no
    def verificar(self):
        if self.condicion == True:
            Mostrar(self.entonces).ver
class MientasQue:
    def __init__(self, condicion, bloque):
        self.condicion = condicion
        self.bloque = bloque

class Mostrar:
    def __init__(self, mensaje):
        self.mensaje = mensaje
    def ver(self):
        print(self.mensaje)