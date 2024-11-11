# 22. Crie um gráfico de dispersão com os pontos coloridos de acordo com seus
# valores usando um mapa de cores (cmap='viridis').

import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(100) * 100
y = np.random.rand(100) * 100
colors = np.sqrt(x**2 + y**2)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, c=colors, cmap='viridis', s=100)
plt.title('Gráfico de Dispersão com Cores Variando')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(label='Magnitude')
plt.grid()
plt.show()
