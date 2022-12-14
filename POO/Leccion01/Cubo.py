class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calcularVolumen(self):
        return self.ancho * self.alto * self.profundo


ancho = float(input('Proporciona el ancho: '))
alto = float(input('Proporciona el alto: '))
profundo = float(input('Proporciona lo profundo: '))

cubo1 = Cubo(ancho, alto, profundo)
print(f'Volúmen cubo: {cubo1.calcularVolumen():.2f}')
