# 23. Faça um gráfico de área (stack plot) para mostrar a evolução de três categorias ao
# longo do tempo, com categorias empilhadas.


import numpy as np
import matplotlib.pyplot as plt

anos = np.arange(2000, 2021)
categoria1 = np.random.randint(1, 10, size=len(anos))
categoria2 = np.random.randint(1, 10, size=len(anos))
categoria3 = np.random.randint(1, 10, size=len(anos))

valores = np.array([categoria1, categoria2, categoria3])

plt.figure(figsize=(10, 6))
plt.stackplot(anos, valores, labels=['Categoria 1', 'Categoria 2', 'Categoria 3'])
plt.title('Evolução de Categorias ao Longo do Tempo')
plt.xlabel('Ano')
plt.ylabel('Valores')
plt.legend(loc='upper left')
plt.grid()
plt.show()
