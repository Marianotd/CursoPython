from Empleado import Empleado
from Gerente import Gerente


def imprimirDetalles(objeto):
    print(objeto)
    print(type(objeto))
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado1 = Empleado('Juan', 5000)
imprimirDetalles(empleado1)

gerente1 = Gerente('Karla', 6000, 'Sistemas')
imprimirDetalles(gerente1)
