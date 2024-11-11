# 4. Crie um array bidimensional (3x3) com números de 1 a 9 e exiba-o.
#

import numpy as np

arr = np.arange(1, 10)

arr_2d = arr.reshape(3, 3)

print(arr_2d)