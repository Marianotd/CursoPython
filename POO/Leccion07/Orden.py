from Producto import Producto


class Orden:
    contadorOrdenes = 0

    @classmethod
    def aumentarContadorOrdenes(cls):
        cls.contadorOrdenes += 1
        return cls.contadorOrdenes

    def __init__(self, productos):
        self._idOrden = Orden.aumentarContadorOrdenes()
        self._productos = list(productos)

    @property
    def idOrden(self):
        return self._idOrden

    @property
    def productos(self):
        return self._productos

    def agregarProducto(self, producto):
        self._productos.append(producto)

    def calcularTotal(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productosStr = ''
        for producto in self.productos:
            productosStr += f'\n{producto.__str__()}'

        return f'Orden: {self._idOrden}, \nProductos: {productosStr}'


if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    producto2 = Producto('Pantalon', 150.00)
    productos1 = [producto1, producto2]
    orden1 = Orden(productos1)
    print(orden1)
    orden2 = Orden(productos1)
    print(orden2)
    