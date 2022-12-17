class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __add__(self, other):
        return f'{self._nombre} {other.nombre}'

    def __sub__(self, other):
        return self._edad - other.edad


persona1 = Persona('Juan', 28)
persona2 = Persona('Carlos', 50)

print(persona1 + persona2)
print(persona1 - persona2)
