# 30. Desenhe um gráfico de linhas múltiplas com diferentes estilos de linha ('--', '-.', ':') e
# adicione uma legenda para cada linha.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, linestyle='--', color='red', label='Seno')
plt.plot(x, y2, linestyle='-.', color='green', label='Cosseno')
plt.plot(x, y3, linestyle=':', color='blue', label='Tangente')
plt.title('Gráfico de Linhas Múltiplas com Estilos Diferentes')
plt.xlabel('x')
plt.ylabel('Valores')
plt.legend()
plt.grid()
plt.show()
