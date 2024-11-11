# 14. Calcule a soma das linhas e das colunas de um array 3x3 com números
# aleatórios.


import numpy as np

array = np.random.randint(0, 10, size=(3, 3))

soma_linhas = np.sum(array, axis=1)