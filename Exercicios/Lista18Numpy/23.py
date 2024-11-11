# 23. Calcule o determinante de uma matriz 3x3 gerada aleatoriamente usando a
# função linalg.det().


import numpy as np

matriz = np.random.rand(3, 3)

determinante = np.linalg.det(matriz)

print(determinante)