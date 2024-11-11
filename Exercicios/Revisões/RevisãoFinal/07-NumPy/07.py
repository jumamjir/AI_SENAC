import numpy as np

array_3d = np.random.rand(5, 5, 5)
soma_matrizes = np.sum(array_3d, axis=(1, 2))
print(soma_matrizes)
