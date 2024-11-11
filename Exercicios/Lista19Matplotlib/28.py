# 28. Crie um gráfico de barras 3D para exibir valores aleatórios em uma grade
# tridimensional (x, y, z).

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(1, 10, 5)
y = np.random.randint(1, 10, 5)
z = np.zeros(5)
dx = dy = np.ones(5)
dz = np.random.randint(1, 10, 5)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.bar3d(x, y, z, dx, dy, dz, alpha=0.7)
ax.set_title('Gráfico de Barras 3D')
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')
plt.show()
