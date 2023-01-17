import math
from decimal import Decimal

# NaN - Not a Numbre (no es un número)
# NaN no es sensible a mayúsculas/minúsculas
# NaN es un tipo de dato numérico indefinido

a = float('NaN')
print(f'a: {a}')
print(f'Es NaN (Not a Number)?: {math.isnan(a)}')

a = Decimal('NaN')
print(f'a: {a}')
print(f'Es NaN (Not a Number)?: {Decimal.is_nan(a)}')
