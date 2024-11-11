# 16. Crie um array de números aleatórios de tamanho 10 e ordene-o em ordem
# crescente.


import numpy as np

array = np.random.rand(10)

array_ordenado = np.sort(array)

print(array_ordenado)