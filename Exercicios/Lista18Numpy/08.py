# 8. Crie dois arrays de 3x3 e realize a multiplicação elemento a elemento (elementwise).

import numpy as np

a1 = np.random.randint(0, 20, 9).reshape(3, 3)
a2 = np.random.randint(0, 20, 9).reshape(3, 3)

print("Array 1:")
print(a1)
print()
print("Array 2:")
print(a2)
print()

array_final = a1 * a2
print("Resultado da multiplicação elemento a elemento:")
print(array_final)
