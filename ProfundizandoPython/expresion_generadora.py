# Expresión generadora (es un generador anónimo)
multiplicacion = (valor * valor for valor in range(4))
# print(multiplicacion)

for valor in multiplicacion:
    print(valor)

# También se puede pasar una expresión generadora a una función (sin paréntesis)

suma = sum(valor * valor for valor in range(4))
print(f'Resultado suma: {suma}')

# Tambien podemos usar una lista o cualquier otro iterador
lista = ['Juan', 'Perez']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))

# Crear un string a partir de un generador creado a partir de una lista
lista = ['Karla', 'Gomez', 22]
contador = 0


# Definimos una función para incrementar el contador
def incrementar():
    global contador
    contador += 1
    return contador


# La primera parte es el yield, la segunda es el for, entre paréntesis
generador = (f'{incrementar()}. {nombre}' for nombre in lista)
lista = list(generador)
print(lista)

cadena = ', '.join(lista)
print(f'Cadena generada: {cadena}')
