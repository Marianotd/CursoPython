# Leer contenido online
from urllib.request import Request
from urllib.request import urlopen


solicitud = Request('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt')
solicitud.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                   'Chrome/97.0.4692.71 Safari/537.36')
mensaje = urlopen(solicitud)
# # contenido = mensaje.read()
# contenido = mensaje.read().decode('utf-8')
# print(contenido)
#
# with open('nuevo_archivo.txt', 'w', encoding='utf-8') as archivo:
#     archivo.write(contenido)


# palabras = []
# for linea in mensaje:
#     palabras_por_linea = linea.decode('utf-8').split()
#
#     for palabra in palabras_por_linea:
#         palabras.append(palabra)
#
# print(palabras)


contenido = mensaje.read().decode('utf-8')

# Contar ocurrencias de una cadena
print(f'N° veces Universidad: {contenido.count("Universidad")}')

# Upper convierte a mayúsculas un str
print(contenido.upper())
print(contenido)

# Lower convierte a minúsculas un str
print(contenido.lower())

# Buscamos la cadena python en el contenido
print(f'Existe python?: {"python".lower() in contenido.lower()}')
print(f'Existe Python?: {"Python".upper() in contenido.upper()}')

# Startswith - Inicia con
print(f'Inicia con: {contenido.startswith("En GlobalMentoring.com.mx")}')

# Endswith - Termina con
print(f'Termina con: {contenido.lower().endswith("globalmentoring.com.mx".lower())} ')


mensaje = 'Hola Mundo'
print(mensaje.lower().islower())
print(mensaje.upper().isupper())


# Alinear cadenas
# Center - Centrar un str
titulo = 'Sitio Web de GlobalMentoring.com.mx'
# print(len(titulo))
# print(titulo.center(50, '-'))
# print(len(titulo.center(50, '-')))
print(titulo.center(len(titulo) + 10, '-'))

# ljust - Alinea a la izquierda
print(titulo.ljust(len(titulo) + 10, '-'))

# rjust - Alinea a la derecha
print(titulo.rjust(len(titulo) + 10, '-'))


# Reemplazar contenido en un str - replace
print(contenido.replace(' ', '-'))

# Eliminar caracteres al inicio y final de un str - strip
titulo = '***GlobalMentoring.com.mx***'
print(f'Cadena original: {titulo}, {len(titulo)}')

titulo = titulo.strip('*')
print(f'Cadena modificada: {titulo}, {len(titulo)}')

titulo = '***GlobalMentoring.com.mx***'.lstrip('*')
print(f'Cadena modificada a la izquierda: {titulo}')

titulo = '***GlobalMentoring.com.mx***'.rstrip('*')
print(f'Cadena modificada a la derecha: {titulo}')

titulo = ' *** GlobalMentoring.com.mx *** '.strip().strip('*').strip()
print(f'Cadena modificada: {titulo}')
