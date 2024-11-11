# 10. Crie um array de 5x5 com números aleatórios e exiba a matriz transposta desse
# array.
import numpy as np

array = np.random.randint(0, 25, 25) .reshape(5, 5)
print(array)
print()
print(array.T)