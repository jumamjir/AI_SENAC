import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)
cores = np.random.rand(100)

ax.scatter(x, y, z, c=cores, alpha=0.6)
ax.set_title('Gráfico 3D de Dispersão')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
