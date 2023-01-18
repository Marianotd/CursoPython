# Bool contiene los valores de True y False
# Tipos numéricos, False para 0, True demás valores
# valor = 0.0
# resultado = bool(valor)
#
# print(f'Valor: {valor}; Resultado: {resultado}')
#
# valor = 15.0
# resultado = bool(valor)
#
# print(f'Valor: {valor}; Resultado: {resultado}')

# Tipo str, False para '', True demás valores
# valor = ''
# resultado = bool(valor)
#
# print(f'Valor: {valor}; Resultado: {resultado}')
#
# valor = 'Hola'
# resultado = bool(valor)
#
# print(f'Valor: {valor}; Resultado: {resultado}')

# Tipo colecciones, False para colecciones vacias, True para todas las demás colecciones
# Lista
# valor = []
# resultado = bool(valor)
#
# print(f'Valor: {valor}; Resultado: {resultado}')
#
# valor = [2, 3, 4]
# resultado = bool(valor)
#
# print(f'Valor: {valor}; Resultado: {resultado}')

# Tupla
# valor = ()
# resultado = bool(valor)
#
# print(f'Valor: {valor}; Resultado: {resultado}')
#
# valor = (2, 3, 4)
# resultado = bool(valor)
#
# print(f'Valor: {valor}; Resultado: {resultado}')

# Diccionario
# valor = {}
# resultado = bool(valor)
#
# print(f'Valor: {valor}; Resultado: {resultado}')
#
# valor = {'nombre': 'Juan', 'apellido': 'Perez'}
# resultado = bool(valor)
#
# print(f'Valor: {valor}; Resultado: {resultado}')


variable = 0
if bool(variable):
    print('Regresó verdadero')

else:
    print('Regresó falso')


if variable:
    print('Regresó verdadero')

else:
    print('Regresó falso')


while variable:
    print('Ejecución ciclo while')

else:
    print('Fin ciclo while')