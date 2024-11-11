# 8. Utilize Matplotlib para exibir um gráfico de barras horizontais com os valores x = [3,
# 8, 1, 10] e rótulos (A, B, C, D).

import matplotlib.pyplot as plt

valoresX = [3, 8, 1, 10]

rotulos = ['A', 'B', 'C', 'D']

plt.bar(rotulos,valoresX,color='red',label='Categoria')
plt.show()



