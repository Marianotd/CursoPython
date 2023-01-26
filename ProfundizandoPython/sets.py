# Profundizar en set
# Un set es una colección de elmentos únicos y es mutable
# Los elementos de un set deben ser inmutables
# conjunto = {[1, 2], [3, 4]}
conjunto = {'Juan', True, 18.0}
print(conjunto)

# Set vacio
# conjunto = {} - Genera un dict vacio
# print(type(conjunto))

# Set vacio correcto
conjunto = set()
print(conjunto)
print(type(conjunto))

# Mutable
conjunto.add('Juan')
print(conjunto)

# Contiene valores únicos
conjunto.add('Juan')
print(conjunto)

# Crear set a partir de un iterable
conjunto = {4, 5, 7, 8, 4}
print(conjunto)

# Podemos agregar más elementos o incluso otro set
conjunto2 = {100, 200, 300, 300}
conjunto.update(conjunto2)
print(conjunto)

conjunto.update([20, 30, 40, 40])
print(conjunto)

# Copiar un set (copia poco profunda, solo copia referencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)

# Verificar igualdad
print(f'Es igual en contenido? {conjunto == conjunto_copia}')
print(f'Es la misma referencia? {conjunto is conjunto_copia}')

# Operaciones de conjuntos con set
# Personas con distintas caracteristicas
pelo_negro = {'Juan', 'Karla', 'Pedro', 'Maria'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_cafe = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'Maria'}

# Todos con ojos_cafe y pelo_rubio (Union) (No se repiten los elementos)
print(ojos_cafe.union(pelo_rubio))

# Invertir el orden con el mismo resultado (conmutativa)
print(pelo_rubio.union(ojos_cafe))

# Intersection - Solo las personas con ojos_cafe y pelo_rubio (conmutativa)
print(ojos_cafe.intersection(pelo_rubio))

# Difference - Pelo_negro sin ojos_cafe (no es conmutativa)
# Las personas que se encuentran en el primer set pero NO en el segundo
print(pelo_negro.difference(ojos_cafe))

# Diferencia simétrica - Personas pelo_negro u ojos_cafe, pero NO ambos (conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))

# Preguntar si un set está contenido en otro (subset)
# Revisamos si los elementos del primer set están contenido en el segundo set
print(menores_30.issubset(pelo_negro))

# Preguntar si un set contiene a otro set (superset)
# Revisar si los elementos del primer set están contenidos en el segundo set
print(menores_30.issuperset(pelo_negro))

# Preguntar si los de pelo_negro no tienen pelo_rubio (disjoint)
print(pelo_negro.isdisjoint(pelo_rubio))
