import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)
cores = x + y

plt.scatter(x, y, c=cores, cmap='viridis')
plt.colorbar(label='Valores')
plt.title('Gráfico de Dispersão')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
