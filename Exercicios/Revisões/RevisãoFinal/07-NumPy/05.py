import numpy as np

array = np.random.rand(25) * 20
array[array > 10] = 10
print(array)
