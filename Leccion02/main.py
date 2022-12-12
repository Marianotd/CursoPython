# operandoA = int(input('Ingrese un número: '))
# operandoB = int(input('Ingrese otro número: '))

# suma = operandoA + operandoB
# print(f'Resultado suma: {suma}')

# resta = operandoA - operandoB
# print(f'Resultado resta: {resta}')

# multiplicacion = operandoA * operandoB
# print(f'Resultado multiplicación: {multiplicacion}')

# division = operandoA / operandoB
# print(f'Resultado división: {division}')

# division = operandoA // operandoB
# print(f'Resultado división (int): {division}')

# modulo = operandoA % operandoB
# print(f'Resultado residuo división (módulo): {modulo}')

# exponente = operandoA ** operandoB
# print(f'Resultado exponente: {exponente}')


# alto = int(input('Proporciona el alto del rectangulo: '))
# ancho = int(input('Proporciona el ancho del rectangulo: '))
# Area = alto * ancho
# Perimetro = (alto + ancho) * 2

# print(f'Area: {Area}')
# print(f'Perimetro: {Perimetro}')

# miVariable = 10
# print(miVariable)

# miVariable = miVariable + 1
# print(miVariable)

# miVariable += 1
# print(miVariable)

# miVariable -= 2
# print(miVariable)

# miVariable *= 3
# print(miVariable)

# miVariable //= 2
# print(miVariable)

# miVariable /= 2
# print(miVariable)


# a = 4
# b = 2

# resultado = a == b
# print(f'Resultado == : {resultado}')

# resultado = a != b
# print(f'Resultado != : {resultado}')

# resultado = a > b
# print(f'Resultado > : {resultado}')

# resultado = a >= b
# print(f'Resultado >= : {resultado}')

# resultado = a < b
# print(f'Resultado < : {resultado}')

# resultado = a <= b
# print(f'Resultado <= : {resultado}')


# a = int(input('Escribe un valor numérico: '))

# if a % 2 == 0:
#     print(f'{a} es número par')
# else:
#     print(f'{a} es número impar')


# edadAdulto = 18
# edadPersona = int(input('Proporciona tu edad: '))

# if edadPersona >= edadAdulto:
#     print(f'La persona con edad {edadPersona} es un adulto')
# else:
#     print(f'La persona con edad {edadPersona} es menor de edad')


# a = True
# b = True
# resultado = a and b
# print(resultado)

# resultado = a or b
# print(resultado)

# resultado = not a
# print(resultado)


# valor = int(input('Escribe el valor: '))
# valorMinimo = 0
# valorMaximo = 5

# dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)

# if dentroRango:
#     print(f'El valor {valor} esta dentro de rango')
# else:
#     print(f'El valor {valor} esta fuera de rango')

# vacaciones = True
# diaDescanso = False

# if vacaciones or diaDescanso:
#     print('Puede asistir al juego')
# else:
#     print('Tiene deberes por hacer')

# vacaciones = False
# diaDescanso = True

# if not (vacaciones or diaDescanso):
#     print('Tiene deberes por hacer')
# else:
#     print('Puede asistir al juego')


# edad = int(input('Introduce tu edad: '))

# veintes = 20 <= edad < 30
# print(veintes)

# treintas = 30 <= edad < 40
# print(treintas)

# if veintes or treintas:
#     print('Dentro de rango (20\'s) o (30\'s)')
#     if veintes:
#         print('Dentro de los 20\'s')
#     elif treintas:
#         print('Dentro de los 30\'s')
#     else:
#         print('Fuera de rango')
# else:
#     print('No está dentro de los 20\'s ni 30\'s')


# edad = int(input('Introduce tu edad: '))

# if 20 <= edad < 30 or 30 <= edad < 40:
#     print('Dentro de rango (20\'s) o (30\'s)')
# else:
#     print('No está dentro de los 20\'s ni 30\'s')

# numero1 = int(input('Proporciona el Número 1: '))
# numero2 = int(input('Proporciona el Número 2: '))

# if numero1 > numero2:
#     print('Número 1 es mayor')
# else:
#     print('Número 2 es mayor')

# print('Proporcione los siguientes datos del libro:')
# nombre = input('Proporciona el nombre: ')
# id = int(input('Proporciona el ID: '))
# precio = float(input('Proporciona el precio: '))
# envioGratuito = input('Indica si el envio es gratuito (True/False): ')

# if envioGratuito == 'True':
#     envioGratuito = True
# elif envioGratuito == 'False':
#     envioGratuito = False
# else:
#     envioGratuito = 'Valor incorrecto, debe escribir True/False'

# print(f'''
# Nombre: {nombre}
# Id: {id}
# Precio: ${precio}
# Envío Gratuito?: {envioGratuito}
# ''')
