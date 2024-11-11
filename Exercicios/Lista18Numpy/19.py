# 19. Crie um array de 10 números e use NumPy para encontrar o índice do maior valor.


import numpy as np

array = np.array([1, 5, 2, 8, 3, 9, 4, 7, 6, 0])

indice_maior_valor = np.argmax(array)

print(indice_maior_valor)