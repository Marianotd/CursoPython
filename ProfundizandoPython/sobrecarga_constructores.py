# Simulación de sobrecarga de constructores en python
# Otras formas de crear objetos
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

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None)

    @classmethod
    def crear_persona_con_valores(cls, nombre, apellido):
        return cls(nombre, apellido)

    def __str__(self):
        return f'Nombre: {self._nombre}, Apellido: {self._apellido}'


persona1 = Persona('Juan', 'Perez')
print(persona1)

persona_vacio = Persona.crear_persona_vacia()
print(persona_vacio)

persona_con_valores = Persona.crear_persona_con_valores('Karla', 'Gomez')
print(persona_con_valores)
