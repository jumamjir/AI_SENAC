# 29. Crie uma matriz 4x4 com valores sequenciais de 1 a 16 e extraia a diagonal
# principal.


import numpy as np

matriz = np.arange(1, 17).reshape(4, 4)

diagonal_principal = np.diag(matriz)

print(diagonal_principal)