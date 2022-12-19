class Monitor:

    contadorMonitor = 0

    @classmethod
    def aumentarContadorMonitor(cls):
        cls.contadorMonitor += 1
        return cls.contadorMonitor

    def __init__(self, marca, tamaño):
        self._idMonitor = self.aumentarContadorMonitor()
        self._marca = marca
        self._tamaño = tamaño

    @property
    def idMonitor(self):
        return self._idMonitor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamaño(self):
        return self._tamaño

    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño

    def __str__(self):
        return f'Id: {self._idMonitor}, Marca: {self._marca}, Tamaño: {self._tamaño} pulgadas'


if __name__ == '__main__':
    monitor1 = Monitor('HP', 15)
    print(monitor1)
    monitor2 = Monitor('Acer', 27)
    print(monitor2)
