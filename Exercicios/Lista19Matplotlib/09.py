# 9. Faça um gráfico de dispersão com 50 pontos aleatórios, variando as cores dos
# pontos com base em um gradiente de valores.



import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.rand(50)
colors = np.linspace(0, 1, 50)

plt.scatter(x, y, c=colors, cmap='viridis', s=100)
plt.grid(True)
plt.show()
