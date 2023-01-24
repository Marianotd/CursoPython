class Persona:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    def __str__(self):
        return f'Nombre: {self._nombre}, Apellido: {self._apellido}, Id: {hex(id(self)).upper()}'


if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez')
    print(persona1)


def mostrar_mensaje(mensaje):
    print(mensaje)
