# 2. Faça um gráfico de dispersão (scatter plot) com os pontos x = [5, 7, 8, 5, 6] e y =
# [10, 14, 12, 15, 16]. Personalize os pontos com a cor azul.

import matplotlib.pyplot as plt

x = [5, 7, 8, 5, 6]
y = [10, 14, 12, 15, 16]

plt.scatter(x,y ,c='blue')
plt.show()