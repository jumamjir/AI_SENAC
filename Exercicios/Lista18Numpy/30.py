# 30. Use NumPy para encontrar os valores únicos em um array com números
# repetidos.


import numpy as np

arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])

valores_unicos = np.unique(arr)

print(valores_unicos)