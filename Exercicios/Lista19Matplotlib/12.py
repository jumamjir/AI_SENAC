# 12. Desenhe um gráfico de linha com estilo de linha tracejada ('--') e cor verde,
# utilizando os valores x = [0, 1, 2, 3] e y = [3, 5, 9, 10].

import matplotlib.pyplot as plt


x = [0, 1, 2, 3]
y = [3, 5, 9, 10]

plt.plot(x,y,linestyle='--',color='green')
plt.show()