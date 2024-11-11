# 4. Faça um histograma de uma distribuição normal de 1000 números aleatórios com
# média 0 e desvio padrão 1. Use 30 bins.

import numpy as np
import matplotlib.pyplot as plt

dados = np.random.normal(0, 1, 1000)


plt.hist(dados, bins=30, color='purple', edgecolor='black')

plt.show()