# 16. Crie um gráfico de linha com um sombreamento (fill_between) entre duas
# funções: y1 = x^2 e y2 = x + 2, para valores de x de 0 a 5.

import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0, 5, 100)
y1 = x ** 2
y2 = x + 2

plt.fill_between(x,y1, y2,where=(y1< y2), color='red', alpha=0.4,label='Áreas Sombreadas')

plt.plot(x,y1, color='blue', alpha=0.6)
plt.plot(x,y2, color='green', alpha=0.6)


plt.grid()
plt.show()
