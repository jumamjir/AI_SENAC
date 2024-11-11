import matplotlib.pyplot as plt
import numpy as np

dados = np.random.normal(loc=0, scale=1, size=1000)
plt.hist(dados, bins=40, alpha=0.7)
plt.title('Histograma de Números Aleatórios')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.show()
