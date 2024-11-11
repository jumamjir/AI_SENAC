# 18. Faça um gráfico de pizza com as porcentagens de 5 categorias, adicione um rótulo
# para cada fatia e um efeito de sombra. Destaque a maior fatia com explode.

import matplotlib.pyplot as plt

produtos = ['A', 'B', 'C', 'D','E']
valores = [30, 15, 5, 25, 25]
explode = (0.1, 0.0, 0, 0.0, 0.0)

plt.pie(valores, labels=produtos, autopct='%1.1f%%', explode=explode, startangle=90,shadow=True)

plt.show()
