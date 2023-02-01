# Decoradores
# Un decorador es una función que recibe una función y regresa otra
# Lo utilizamos para extender funcionalidad

# 1. Función decorador (a)
# 2. Función a decorar (b)
# 3. Función decorada (c)

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c():
        funcion_a_decorar_b

    return funcion_decorada_c


@funcion_decorador_a
def mostrar_mensaje():
    print('Hola desde función mostrar mensaje')


mostrar_mensaje()
