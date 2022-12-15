class Producto:
    contadorProductos = 0

    @classmethod
    def aumentarContadorProductos(cls):
        cls.contadorProductos += 1
        return cls.contadorProductos

    def __init__(self, nombre, precio):
        self._idProducto = Producto.aumentarContadorProductos()
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f'Producto[Id: {self._idProducto}, Nombre: {self._nombre}, Precio: {self._precio}]'


if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    print(producto1)
    producto2 = Producto('Pantalon', 150.00)
    print(producto2)
