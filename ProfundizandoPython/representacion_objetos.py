# Representación de objetos (str, repr, format)
# print(dir(object))

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

    # repr, más enfocado a los programadores
    def __repr__(self):
        return f'{self.__class__.__name__}(nombre:{self._nombre}, apellido:{self._apellido})'

    # str es más para el usuario final u otros sistemas
    # la implementación por default llama al método repr
    def __str__(self):
        return f'{self.__class__.__name__}: {self._nombre} {self._apellido}'

    # format su implementación por default es str
    # se manda a llamar al usar f-string
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre {self._nombre} y apellido {self._apellido}'


persona1 = Persona('Juan', 'Perez')
# repr (!r)
print(f'Mi objeto persona1: {persona1!r}')

# str (de manera automática el método print llama al método str)
print(persona1)

# format
print(f'{persona1}')
