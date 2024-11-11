# 26. Crie um array de 10 elementos e substitua os valores negativos por zero usando a
# função where().


import numpy as np

arr = np.array([1, -2, 3, -4, 5, -6, 7, -8, 9, -10])

arr = np.where(arr < 0, 0, arr)

print(arr)
