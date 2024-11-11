# 25. Gere um array de 100 números aleatórios e exiba o histograma desses valores.


import numpy as np

dados = np.random.randn(100)

hist, bins = np.histogram(dados, bins=10)

print("Histograma:")
print(hist)
print("Bins:")
print(bins)
