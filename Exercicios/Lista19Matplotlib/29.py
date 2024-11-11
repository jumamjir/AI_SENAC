# 29. Faça um gráfico de linha com a função sigmoide e destaque a área de
# crescimento rápido usando fill_between.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
sigmoide = 1 / (1 + np.exp(-x))

plt.figure(figsize=(10, 6))
plt.plot(x, sigmoide, label='Função Sigmoide', color='blue')
plt.fill_between(x, sigmoide, where=(sigmoide > 0.5), color='orange', alpha=0.5)
plt.title('Função Sigmoide com Área de Crescimento Rápido')
plt.xlabel('x')
plt.ylabel('Sigmoide(x)')
plt.legend()
plt.grid()
plt.show()
