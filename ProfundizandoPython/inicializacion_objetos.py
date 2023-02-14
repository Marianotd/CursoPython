# Orden de inicialzación de objetos
class Padre:
    def __init__(self):
        print('Inicializador Padre')

    def metodo(self):
        print('Método padre')


class Hijo(Padre):
    # Se manda a llamar el método __init__ de la clase padre
    # siempre y cuando la clase hija no defina su propio método init

    # Definimos el método init
    def __init__(self):
        # De manera opcional podemos llamar al método init de la clase padre (super)
        print('Inicializador Hijo')
        super().__init__()

    # Sobreescribimos el método heredado de la clase padre
    def metodo(self):
        print('Método sobreescrito hijo')
        super().metodo()

# padre1 = Padre()
# padre1.metodo()

hijo1 = Hijo()
hijo1.metodo()
