# 26. Faça um gráfico de dispersão com pontos de diferentes tamanhos baseados em
# um terceiro array (sizes = [30, 60, 90, 120, 150]).

import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(10) * 100
y = np.random.rand(10) * 100
sizes = [30, 60, 90, 120, 150, 30, 60, 90, 120, 150]

plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=sizes, alpha=0.5)
plt.title('Gráfico de Dispersão com Tamanhos Variáveis')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
