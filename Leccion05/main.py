# nombres = ['Juan', 'Karla', 'Ricardo', 'María']
#
# print(nombres)
# print(nombres[0])
#
# print(nombres[0:2])
# print(nombres[:3])
# print(nombres[1:])
#
# nombres[3] = 'Ivone'
# print(nombres)
#
# for nombre in nombres:
#     print(nombre)
# else:
#     print('No existen más nombres en la lista')
#
# print(len(nombres))
#
# nombres.append('Lorenzo')
# print(nombres)
#
# nombres.insert(1, 'Octavio')
# print(nombres)
#
# nombres.remove('Octavio')
# print(nombres)
#
# nombres.pop()
# print(nombres)
#
# del nombres[0]
# print(nombres)
#
# nombres.clear()
# print(nombres)
#
# del nombres

# print('Rango de 0 a 10 con números divisibles entre 3')
# for i in range(11):
#     if i % 3 == 0 and i != 0:
#         print(i)
#
# print('Rango con valores de inicio = 2 y fin = 6')
# rango = range(2, 7)
#
# for i in rango:
#     print(i)
#
# print('Rango con valores de inicio = 3, fin = 10 e incremento = 2')
# rango = range(3, 11, 2)
#
# for i in rango:
#     print(i)

# frutas = ('Naranja', 'Platano', 'Guayaba')
# print(frutas)
#
# print(len(frutas))
#
# print(frutas[0])
#
# print(frutas[-1])
#
# print(frutas[0:1])
#
# for fruta in frutas:
#     print(fruta, end=' ')
#
# # frutas[0] = 'Pera'
# frutasLista = list(frutas)
# frutasLista[0] = 'Pera'
# frutas = tuple(frutasLista)
#
# print('\n', frutas)
#
# del frutas

# tupla = (13, 1, 8, 3, 2, 5, 8)
# lista = []
#
# for elemento in tupla:
#     if elemento < 5:
#         lista.append(elemento)
#
# print(lista)

# planetas = {'Marte', 'Júpiter', 'Venus'}
# print(planetas)
#
# print(len(planetas))
#
# print('Marte' in planetas)
#
# planetas.add('Tierra')
# print(planetas)
#
# planetas.add('Tierra')
# print(planetas)
#
# planetas.remove('Tierra')
# print(planetas)
#
# planetas.discard('Júpiter')
# print(planetas)
#
# planetas.clear()
# print(planetas)
#
# del planetas

# diccionario = {
#     'IDE': 'Integrated Development Enviroment',
#     'OOP': 'Object Oriented Programming',
#     'DBMS': 'Database Managment System'
# }
#
# print(diccionario)
# print(len(diccionario))
#
# print(diccionario['IDE'])
# print(diccionario.get('OOP'))
#
# diccionario['IDE'] = 'integrated development environment'
# print(diccionario)
#
# for termino, valor in diccionario.items():
#     print(f'{termino}: {valor}')
#
# for termino in diccionario.keys():
#     print(termino)
#
# for valor in diccionario.values():
#     print(valor)
#
# print('IDE' in diccionario)
#
# diccionario['PK'] = 'Primary Key'
# print(diccionario)
#
# diccionario.pop('DBMS')
# print(diccionario)
#
# diccionario.clear()
# print(diccionario)
#
# del diccionario

