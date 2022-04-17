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

'''
bloque_alternativa.agregarInstruccion(alternativa)
bucle = MientrasQue(True, bloque_alternativa)'''