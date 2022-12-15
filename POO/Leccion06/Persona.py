class Persona:
    contadorPersonas = 0

    @classmethod
    def generarSiguienteValor(cls):
        cls.contadorPersonas += 1
        return cls.contadorPersonas

    def __init__(self, nombre, edad):
        self.idPersona = Persona.generarSiguienteValor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona[Id: {self.idPersona}, Nombre: {self.nombre}, Edad: {self.edad}]'


persona1 = Persona('Juan', 28)
print(persona1)
persona2 = Persona('Karla', 30)
print(persona2)
persona3 = Persona('Eduardo', 25)
print(persona3)
Persona.generarSiguienteValor()
persona4 = Persona('Maria', 35)
print(persona4)

print(f'Valor contador personas: {Persona.contadorPersonas}')
