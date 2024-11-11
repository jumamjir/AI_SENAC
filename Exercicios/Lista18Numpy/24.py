# 24. Crie um array de tamanho 8 e transforme-o em uma matriz 2x4. Exiba o novo array.

import numpy as np

array = np.arange(8)

matriz = array.reshape(2, 4)

print(matriz)