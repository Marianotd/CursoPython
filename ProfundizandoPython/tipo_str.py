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
# cursos = 'Java Python Javascript Angular Spring Excel'
# lista_cursos = cursos.split()
# print(f'Lista cursos: {lista_cursos}')
# print(type(lista_cursos))
#
#
# cursos_separados_coma = 'Java, Python, Javascript, Angular, Spring, Excel'
# lista_cursos = cursos_separados_coma.split(', ')
# print(f'Lista cursos separados por coma: {lista_cursos}')
# print(len(lista_cursos))
#
#
# lista_cursos = cursos_separados_coma.split(', ', 3)
# print(f'Lista cursos: {lista_cursos}')
# print(len(lista_cursos))


# Dar formato a un str
# nombre = 'Juan'
# edad = 28
# mensaje_con_formato = 'Mi nombre es %s y tengo %d años' % (nombre, edad)
# print(mensaje_con_formato)


# persona = ('Karla', 'Gomez', 5000.00)
# mensaje_con_formato = 'Hola %s %s. Tu sueldo es $%.2f' % persona
# print(mensaje_con_formato)

# mensaje_con_formato = 'Hola %s %s. Tu sueldo es $%.2f'
# print(mensaje_con_formato % persona)


# nombre = 'Juan'
# edad = 28
# sueldo = 3000

# mensaje = f'Nombre: {nombre}; Edad: {edad}; Sueldo: ${sueldo:.2f}'
# print(mensaje)

# mensaje = 'Nombre: {}; Edad: {}; Sueldo: ${:.2f}'.format(nombre, edad, sueldo)
# print(mensaje)
#
# mensaje = 'Nombre: {}; Edad: {}; Sueldo: ${:.2f}'
# print(mensaje.format(nombre, edad, sueldo))

# mensaje = 'Nombre: {0}; Edad: {1}; Sueldo: ${2:.2f}'.format(nombre, edad, sueldo)
# print(mensaje)

# mensaje = 'Sueldo: ${2:.2f}; Nombre: {0}; Edad: {1}'.format(nombre, edad, sueldo)
# print(mensaje)

# mensaje = 'Nombre: {n}; Edad: {e}; Sueldo: ${s:.2f}'.format(n=nombre, e=edad, s=sueldo)
# print(mensaje)

# diccionario = {'nombre': 'Ivan', 'edad': 35, 'sueldo': 8000.00}
# mensaje = 'Nombre: {p[nombre]}; Edad: {p[edad]}; Sueldo: ${p[sueldo]:.2f}'.format(p=diccionario)
# print(mensaje)

# Método print
# print(nombre, edad, sueldo, sep=', ')


# Multiplicación str
# resultado = 3 * 'Hola'
# print(f'Resultado: {resultado}')

# Multiplicación tuplas
# resultado = 5 * ('Hola', 10)
# print(f'Resultado: {resultado}')

# Multiplicación listas
# resultado = 10 * [0]
# print(f'Resultado: {resultado}, largo: {len(resultado)}')


# Caracteres de escape
# resultado = 'Hola \' Mundo'
# print(f'Resultado: {resultado}')
#
# resultado = 'Se va a eliminar el punto.\b\b\b'
# print(f'Resultado: {resultado}')

# Caracter /
# resultado = 'c:\\directorio\\juan'
# print(f'Resultado: {resultado}')

# Row string
# resultado = r'c:\directorio\juan'
# print(f'Resultado: {resultado}')


# Caracteres unicode
# print('Hola\u0020Mundo')
# print('Notación simple: \u0041')
# print('Notación extendida: \U00000041')
# print('Notación hexadecimal: \x41')
# print('Mano: \u270C')
# print('Cara sonriendo: \U0001f600')
# print('Serpiente: \U0001F40D')



# Caracteres ascii
# caracter = chr(65)
# print('A mayúscula:', caracter)
#
# caracter = chr(64)
# print('Símbolo @:', caracter)
#
# caracter = chr(97)
# print('a minúscula:', caracter)



# 