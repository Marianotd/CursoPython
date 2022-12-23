import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            # sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            # # llaves_primarias = ((1, 2, 3),)
            # entrada = input('Proporciona los id\'s a buscar (separado por comas): ')
            # llaves_primarias = (tuple(entrada.split(',')),)
            # cursor.execute(sentencia, llaves_primarias)
            # registros = cursor.fetchall()
            # for registro in registros:
            #     print(registro)

            # sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            # valores = (
            #     ('Marcos', 'Cantu', 'mcantu@mail.com'),
            #     ('Angel', 'Quintana', 'aquintana@mail.com'),
            #     ('Maria', 'Gonzalez', 'mgonzalez@mail.com')
            # )
            # cursor.executemany(sentencia, valores)
            # registros_insertados = cursor.rowcount
            # print(f'Registros Insertados: {registros_insertados}')

            # sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
            # valores = (
            #     ('Juan', 'Perez', 'jperez@mail.com', 1),
            #     ('Ivonne', 'Gutierrez', 'igutierrez@mail.com', 2)
            # )
            # cursor.executemany(sentencia, valores)
            # registros_actualizados = cursor.rowcount
            # print(f'Registros Actualizados: {registros_actualizados}')

            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona los id_persona a eliminar (separados por coma): ')
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros Eliminados: {registros_eliminados}')

except Exception as e:
    print(f'Ocurrió un error: {e}')

finally:
    conexion.close()
