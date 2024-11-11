# 14. Faça um gráfico de área preenchida (fill plot) com a função seno de 0 a 2π. Utilize
# uma cor transparente.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)

y = np.sin(x)

plt.fill_between(x,y, color='blue',alpha=0.1)

plt.grid()
plt.show()


