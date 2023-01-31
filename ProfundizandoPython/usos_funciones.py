# Las funciones en python son ciudadanas de primera clase
# First class citizens

# Definimos la función
def sumar(a, b):
    return a + b


# 1. Asignar una función a una variable (no se usan parentesis)
mi_funcion = sumar

# Verificar el tipo de variable
print(type(mi_funcion))

# Llamamos la función a través de la variable
resultado = mi_funcion(5, 8)
print(f'Resultado: {resultado}')


# 2. Función como argumento
def operacion(a, b, sumar_args):
    print(f'Resultado sumar: {sumar_args(a, b)}')


operacion(4, 5, sumar)


# 3. Podemos retornar una función
def retornar_funcion():
    # Retornamos una función
    return sumar


mi_funcion_retornada = retornar_funcion()
print(f'Resultado función retornada: {mi_funcion_retornada(5, 7)}')
