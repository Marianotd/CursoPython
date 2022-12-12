# def miFuncion(nombre, apellido):
#     print('Saludos desde mi función')
#     print(f'Nombre: {nombre}, Apellido: {apellido}')
#
#
# miFuncion('Juan', 'Perez')
# miFuncion('Karla', 'Lara')

# def sumar(a=0, b=0):
#     return a + b
#
#
# resultado = sumar(5, 3)
# print(f'Resultado sumar: {resultado}')

# def listarNombres(*args):
#     for nombre in args:
#         print(nombre)
#
#
# listarNombres('Juan', 'Karla', 'Maria', 'Ernesto')
# listarNombres('Laura', 'Carlos')


# def sumarValores(*args):
#     resultado = 0
#     for valor in args:
#         resultado += valor
#     return resultado
#
#
# print(sumarValores(3, 5, 9, 4, 6))


# def multiplicarValores(*args):
#     resultado = 1
#     for numero in args:
#         resultado *= numero
#     return resultado
#
#
# print(multiplicarValores(2, 2, 2))


# def listarTerminos(**kwargs):
#     for llave, valor in kwargs.items():
#         print(f'{llave}: {valor}')
#
#
# listarTerminos(IDE='Integrated Development Environment', PK='Primary Key')
# listarTerminos(DBMS='Database Menagement System')


# def desplegarNombres(nombres):
#     for nombre in nombres:
#         print(nombre)
#
#
# nombres = ['Juan', 'Karla', 'Guillermo']
#
# desplegarNombres(nombres)
# desplegarNombres('Carlos')
# desplegarNombres((10, 11))


# def factorial(numero):
#     if numero == 1:
#         return 1
#     else:
#         return numero * factorial(numero - 1)
#
#
# numero = 3
# resultado = factorial(numero)
# print(f'El factorial de {numero} es: {resultado}')


# def imprimirNumeroRecursivo(numero):
#     if numero >= 1:
#         print(numero)
#         imprimirNumeroRecursivo(numero - 1)
#     elif numero == 0:
#         return
#     else:
#         print('Valor Incorrecto...')
#
#
# imprimirNumeroRecursivo(5)


# def calcularTotalPago(pagoSinImpuesto, impuesto):
#     pagoTotal = pagoSinImpuesto + pagoSinImpuesto * (impuesto / 100)
#     return pagoTotal
#
#
# pagoSinImpuesto = float(input('Proporcione el pago sin impuestos: '))
# impuesto = float(input('Proporcione el monto del impuesto: '))
#
# print(calcularTotalPago(pagoSinImpuesto, impuesto))


# def celsius_fahrenheit(celsius):
#     return celsius * 9 / 5 + 32
#
#
# def fahrenheit_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5 / 9
#
#
# celsius = float(input('Proporcione su valor en celsius: '))
# resultado = celsius_fahrenheit(celsius)
#
# print(f'{celsius} C a F: {resultado}')
#
# fahrenheit = float(input('Proporcione su valor en fahrenheit: '))
# resultado = fahrenheit_celsius(fahrenheit)
#
# print(f'{fahrenheit} F a C: {resultado:.1f}')


