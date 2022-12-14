class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura


base = float(input('Proporciona la base: '))
altura = float(input('Proporciona la altura: '))

rectangulo1 = Rectangulo(base, altura)
print(f'Área rectángulo: {rectangulo1.calcularArea():.2f}')
