try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adios\n')
    archivo.write('Última linea')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Fin del archivo'.center(50, '-'))
