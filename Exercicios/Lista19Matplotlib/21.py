# 21. Plote um gráfico de linha usando a função log(x) com valores de x variando de 1 a
# 100. Personalize o estilo da linha e adicione marcadores ('o').


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 100, 100)
y = np.log(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, linestyle='--', color='purple', marker='o', markersize=5)
plt.title('Gráfico da Função log(x)')
plt.xlabel('x')
plt.ylabel('log(x)')
plt.grid()
plt.show()
