from mundo_pc.DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contadorTeclados = 0

    @classmethod
    def aumentarContadorTeclados(cls):
        cls.contadorTeclados += 1
        return cls.contadorTeclados

    def __init__(self, marca, tipoEntrada):
        super().__init__(marca, tipoEntrada)
        self._idTeclado = self.aumentarContadorTeclados()

    @property
    def idTeclado(self):
        return self._idTeclado

    def __str__(self):
        return f'Id: {self._idTeclado}, Marca: {self.marca}, Tipo_entrada: {self.tipoEntrada}'


if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    print(teclado1)
    teclado2 = Teclado('Gamer', 'Bluetooth')
    print(teclado2)
