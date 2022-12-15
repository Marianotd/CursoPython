from abc import ABC, abstractmethod


def _validarValor(valor):
    return True if 0 < valor < 10 else False


class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if _validarValor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo ancho: {ancho}')
        if _validarValor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo alto: {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if _validarValor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if _validarValor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')

    @abstractmethod
    def calcularArea(self):
        pass

    def __str__(self):
        return f'Figura Geométrica[Ancho: {self._ancho}, Alto: {self._alto}]'
