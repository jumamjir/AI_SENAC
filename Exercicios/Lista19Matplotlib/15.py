# 15. Desenhe um gráfico polar com os ângulos de 0 a 2π e os raios variando de 0 a 10.
# Personalize a cor da linha.

import matplotlib.pyplot as plt
import numpy as np

angulos = np.linspace(0, 2 * np.pi,10)
raios = np.linspace(0, 10, 10)

plt.polar(angulos,raios, marker='d',color='red')

plt.show()



