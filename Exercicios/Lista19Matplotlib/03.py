# 3. Crie um gráfico de barras com os meses do ano (Jan a Jun) e os valores (5, 7, 8, 6,
# 2, 9). Adicione rótulos aos eixos e um título ao gráfico.

import matplotlib.pyplot as plt

x = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
y = [5, 7, 8, 6, 2, 9]

plt.bar(x,y, color='blue')

plt.title("Graficozao")
plt.xlabel('Meses')
plt.ylabel('Valores')
plt.show()
