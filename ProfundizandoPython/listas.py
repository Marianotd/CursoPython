# Profundizando en listas
# Listas son mutables
nombres1 = ['Juan', 'Karla', 'Pedro']
nombres2 = 'Laura Maria Gonzalo Ernesto'.split()

# Sumar listas
print(f'Sumar listas: {nombres1 + nombres2}')

# Extender una lista con otra lista
nombres1.extend(nombres2)
print(f'Extender la lista1 con la lista2: {nombres1}')
