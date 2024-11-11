# 21. Crie um DataFrame com dados de uma função polinomial usando NumPy (x^2,
# x^3). Exiba gráficos de linha para cada função usando diferentes estilos de linha.


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y1 = x**2
y2 = x**3

plt.plot(x, y1, label='y = x^2', linestyle='-')
plt.plot(x, y2, label='y = x^3', linestyle='--')
plt.title('Funções Polinomiais')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()







