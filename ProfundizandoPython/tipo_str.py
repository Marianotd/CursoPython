# Profundizando en el tipo str
# import string

# Concatenación automática en python
# variable = 'Adios'
# mensaje = 'Hola' 'Mundo' + variable
# mensaje += 'Universidad' 'Python'
#
# print(mensaje)


# import math
#
# # Help
# help(math.isnan)
# help(str.capitalize)


# from mi_clase import MiClase
#
# # help(MiClase)
# print(MiClase.__doc__)
# print(MiClase.__init__.__doc__)
# print(MiClase.mi_metodo.__doc__)
# print(MiClase.mi_metodo)
# print(type(MiClase.mi_metodo))


# help(str.capitalize)
# mensaje1 = 'hola mundo'
# mensaje2 = mensaje1.capitalize()
#
# print(f'mensaje1: {mensaje1}, id: {hex(id(mensaje1))}')
# print(f'mensaje2: {mensaje2}, id: {hex(id(mensaje2))}')
#
# mensaje1 += 'adios'
#
# print(f'mensaje1: {mensaje1}, id: {hex(id(mensaje1))}')


# help(str.join)
# tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')
# mensaje = ' '.join(tupla_str)
# print(f'Mensaje: {mensaje}')
#
# lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
# mensaje = ', '.join(lista_cursos)
# print(f'Mensaje: {mensaje}')
#
# cadena = 'HolaMundo'
# mensaje = '.'.join(cadena)
# print(f'Mensaje: {mensaje}')
#
# diccionario = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': '18'}
# llaves = ' - '.join(diccionario.keys())
# valores = ' - '.join(diccionario.values())
# print(f'Llaves: {llaves}, type: {type(llaves)}')
# print(f'Valores: {valores}, type: {type(valores)}')


# help(str.split)
cursos = 'Java Python Javascript Angular Spring Excel'
lista_cursos = cursos.split()
print(f'Lista cursos: {lista_cursos}')
print(type(lista_cursos))


cursos_separados_coma = 'Java, Python, Javascript, Angular, Spring, Excel'
lista_cursos = cursos_separados_coma.split(', ')
print(f'Lista cursos separados por coma: {lista_cursos}')
print(len(lista_cursos))


lista_cursos = cursos_separados_coma.split(', ', 3)
print(f'Lista cursos: {lista_cursos}')
print(len(lista_cursos))
