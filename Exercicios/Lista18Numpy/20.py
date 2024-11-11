# 20. Utilize NumPy para criar um array de valores aleatórios entre 0 e 1 e arredonde
# todos os elementos para uma casa decimal.


import numpy as np

array = np.random.rand(10)

array_arredondado = np.round(array, decimals=1)

print(array_arredondado)

