import numpy as np

array_2d = np.random.rand(4, 4) * 20
media = np.mean(array_2d)
array_2d[array_2d < media] = 0
print(array_2d)
