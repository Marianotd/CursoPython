class Orden:
    contadorOrdenes = 0

    @classmethod
    def aumentarContadorOrdenes(cls):
        cls.contadorOrdenes += 1
        return cls.contadorOrdenes

    def __init__(self, computadoras):
        self._idOrden = self.aumentarContadorOrdenes()
        self._computadoras = list(computadoras)

    @property
    def idOrden(self):
        return self._idOrden

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = computadoras

    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadorasStr = ''
        for computadora in self._computadoras:
            computadorasStr += computadora.__str__()

        return f'''
Orden: {self._idOrden}
Computadoras: {computadorasStr}
        '''
