# 15. Substitua todos os elementos menores que 5 em um array por zero e exiba o
# resultado.


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

arr[arr < 5] = 0

print(arr)