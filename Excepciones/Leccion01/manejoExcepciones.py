from NumerosIdenticosException import NumerosIdenticosException

resultado = None

try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    if a == b:
        raise NumerosIdenticosException('Números idénticos')
    else:
        resultado = a / b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {e}')
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {e}')
except ValueError as e:
    print(f'ValueError - Ocurrió un error: {e}')
except NumerosIdenticosException as e:
    print(f'NumerosIdenticosException - Ocurrió un error: {e}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {e}')
else:
    print(f'Resultado: {resultado:.2f}')
finally:
    print(f'Continuamos'.center(50, '-'))
