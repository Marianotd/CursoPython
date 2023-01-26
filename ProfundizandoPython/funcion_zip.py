# print(dir(__builtins__))
# help(zip)

numeros = (1, 2, 3)
letras = ['a', 'b', 'c', 'd']
identificadores = 321, 322, 323, 324, 325
conjunto = {6, 4, 0, 9, 8, 15, 10}

mezcla = zip(numeros, letras, identificadores, conjunto)

# print(mezcla)
print(list(mezcla))
# print(tuple(zip(numeros, letras)))
# print(type(mezcla))


# Iterar en paralelo
for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
    print(f'Número: {numero}, Letra: {letra}, Id: {id}, Aleatorio: {aleatorio}')


nueva_lista = []
for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
    nueva_lista.append(f'{id} - {numero} - {letra} - {aleatorio}')

print(nueva_lista)

# Unzip
mezcla = [(1, 'a'), (2, 'b'), (3, 'c')]
numeros, letras = zip(*mezcla)

print(f'Numeros: {numeros}, Letras: {letras}')

# Ordenamiento usando zip
letras = ['c', 'd', 'a', 'e', 'b']
numeros = [3, 2, 4, 1, 0]

mezcla = zip(letras, numeros)

# Sin ordenar
print(tuple(mezcla))

# Ordenar por letra (primer iterable)
print(sorted(zip(letras, numeros)))

# Crear un diccionario con zip y dos iterables
llaves = ['Nombre', 'Apellido', 'Edad']
valores = ['Juan', 'Perez', 18]

diccionario = dict(zip(llaves, valores))
print(diccionario)

# Actualizar un elemento de un diccionario
llave = ['Edad']
nueva_edad = [28]

diccionario.update(zip(llave, nueva_edad))
print(diccionario)
