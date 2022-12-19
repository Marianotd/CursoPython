try:
    archivo = open('prueba.txt', 'r', encoding='utf8')
    # print(archivo.read())

    # print(archivo.read(5))
    # print(archivo.read(3))

    # print(archivo.readline())
    # print(archivo.readline())

    # for line in archivo:
    #     print(line)

    # print(archivo.readlines())

    # print(archivo.readlines()[1])

    archivo2 = open('copia.txt', 'a', encoding='utf8')
    archivo2.write(archivo.read())
finally:
    archivo.close()
    archivo2.close()
    print('Fin proceso lectura y escritura de archivos'.center(50, '-'))
