from Orden import Orden
from Producto import Producto

producto1 = Producto('Camisa', 100.00)
producto2 = Producto('Pantalon', 150.00)
producto3 = Producto('Calcetines', 50.00)
producto4 = Producto('Blusa', 70.00)

productos1 = [producto1, producto2]
productos2 = [producto3, producto3]

orden1 = Orden(productos1)
orden1.agregarProducto(producto3)
orden1.agregarProducto(producto4)
print(orden1)
print(f'Total orden1: {orden1.calcularTotal()}\n')

orden2 = Orden(productos2)
print(orden2)
print(f'Total orden2: {orden2.calcularTotal()}\n')
