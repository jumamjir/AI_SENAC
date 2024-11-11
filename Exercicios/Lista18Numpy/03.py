# 3. Crie um array de 10 números inteiros aleatórios entre 0 e 50. Exiba o array e seu
# maior e menor valor.


import numpy as np
a = np.random.randint(0, 50, 10)
print(a)

print("Maior valor:", a.max())
print("Menor valor:", a.min())