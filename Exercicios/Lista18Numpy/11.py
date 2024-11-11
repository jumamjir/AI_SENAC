# 11. Crie um array com os números de 1 a 10 e exiba apenas os números pares.


import numpy as np

a = np.arange(1, 11)
even_numbers = a[a % 2 == 0]

print(even_numbers)