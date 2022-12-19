class ManejoArchivos:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __enter__(self):
        print('Obtenemos el recurso'.center(50, '-'))
        self._nombre = open(self._nombre, 'r', encoding='utf8')
        return self._nombre

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Cerramos el recurso'.center(50, '-'))
        if self._nombre:
            self._nombre.close()
