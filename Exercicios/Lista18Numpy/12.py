# 12. Faça um slice de um array 4x4, exibindo apenas os elementos da segunda e
# terceira colunas.


import numpy as np

array = np.arange(16).reshape(4, 4)

sliced_array = array[:, 1:3]

print(sliced_array)