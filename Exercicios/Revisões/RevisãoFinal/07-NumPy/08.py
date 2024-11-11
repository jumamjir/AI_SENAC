import numpy as np

matriz_identidade = np.eye(6)
matriz_identidade[np.diag_indices(6)] = np.arange(1, 7)
print(matriz_identidade)
