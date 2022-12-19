from mundo_pc.Monitor import Monitor
from mundo_pc.Raton import Raton
from mundo_pc.Teclado import Teclado


class Computadora:
    contadorComputadoras = 0

    @classmethod
    def aumentarContadorComputadoras(cls):
        cls.contadorComputadoras += 1
        return cls.contadorComputadoras

    def __init__(self, nombre, monitor, teclado, raton):
        self._idComputadora = self.aumentarContadorComputadoras()
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def idComputadora(self):
        return self._idComputadora

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f'''
    {self._nombre}: {self._idComputadora}
    Monitor: {self._monitor}
    Teclado: {self._teclado}
    Ratón: {self._raton}
        '''


if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('HP', 15)
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)

    teclado2 = Teclado('Acer', 'Bluetooth')
    raton2 = Raton('Acer', 'Bluetooth')
    monitor2 = Monitor('Acer', 27)
    computadora2 = Computadora('Acer', monitor2, teclado2, raton2)
    print(computadora2)
