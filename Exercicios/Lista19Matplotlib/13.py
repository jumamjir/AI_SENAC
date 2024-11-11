# 13. Crie um gráfico de barras agrupadas para comparar os valores A = [4, 5, 6] e B = [2,
# 3, 5] em três categorias (Cat1, Cat2, Cat3).

import matplotlib.pyplot as plt
import numpy as np

categorias = ['Cat1', 'Cat2', 'Cat3']

valoresA = [4, 5, 6]
valoresB = [2,3, 5]

largura = 0.35
x = np.arange(len(categorias))

plt.bar(x - largura/2, valoresA, largura, color='red', label='Valores A')
plt.bar(x + largura/2, valoresB, largura, color='blue', label='Valores B')
plt.xlabel('Categorias')

plt.legend()
plt.show()
