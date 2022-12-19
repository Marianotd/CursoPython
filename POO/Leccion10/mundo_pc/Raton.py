from mundo_pc.DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contadorRatones = 0

    @classmethod
    def aumentarContadorRatones(cls):
        cls.contadorRatones += 1
        return cls.contadorRatones

    def __init__(self, marca, tipoEntrada):
        super().__init__(marca, tipoEntrada)
        self._idRaton = self.aumentarContadorRatones()

    @property
    def idRaton(self):
        return self._idRaton

    def __str__(self):
        return f'Id: {self._idRaton}, Marca: {self.marca}, Tipo_entrada: {self.tipoEntrada}'


if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    print(raton1)

    raton2 = Raton('Acer', 'Bluetooth')
    print(raton2)
