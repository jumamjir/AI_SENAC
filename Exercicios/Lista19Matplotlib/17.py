# 17. Exiba um gráfico de dispersão 3D com os pontos aleatórios em um espaço
# tridimensional (x, y, z). Use cores e tamanhos variados para os pontos.

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)
colors = np.random.rand(50)
sizes = np.random.randint(20, 200, size=50)

scatter = ax.scatter(x, y, z, c=colors, s=sizes, cmap='viridis', alpha=0.6)

plt.colorbar(scatter, label='Cor dos Pontos')
plt.show()

