from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas

opcion = None

while opcion != 4:
    try:
        print('Opciones'.center(50, '-'))
        print('1. Agregar Película')
        print('2. Listar Peliculas')
        print('3. Eliminar catálogo de peliculas')
        print('4. Salir')
        opcion = int(input('Escribe tu opción(1-4): '))

        if opcion == 1:
            nombrePelicula = input('Proporciona el nombre de la pelicula: ')
            pelicula = Pelicula(nombrePelicula)
            CatalogoPeliculas.AgregarPelicula(pelicula)

        elif opcion == 2:
            CatalogoPeliculas.listarPeliculas()

        elif opcion == 3:
            CatalogoPeliculas.eliminarPeliculas()

        else:
            print(f'Opción incorrecta: {opcion}. Debe ingresar un valor entre 1 y 4')

    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion = None

else:
    print('Salimos del programa'.center(50, '-'))
