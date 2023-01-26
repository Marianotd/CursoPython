# Profundizando en tuplas

# Declarar variables
a, b = 'Hola', 'Adios'
print(a, b)

# Swap (intercambio)
a, b = b, a
print(a, b)


# Regresar múltiples valores en una función
def minmax(elementos):
    return min(elementos), max(elementos)


min, max = minmax(list(range(1, 5)))
print(f'Valor min: {min}, Valor max: {max}')

# Regresa la suma de una tupla
resultado = sum((1, 2, 3, 4, 5))
print(f'Resultado: {resultado}')

def sumar(*args):
    return sum(args)


resultado = sumar(1, 2, 3, 4, 5)
print(f'Resultado: {resultado}')
