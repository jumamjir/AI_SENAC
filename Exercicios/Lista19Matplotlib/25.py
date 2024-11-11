# 25. Plote um gráfico com múltiplas linhas, cada uma representando uma função
# polinomial diferente (x^2, x^3, x^4) no mesmo intervalo.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y2 = x**2
y3 = x**3
y4 = x**4

plt.figure(figsize=(10, 6))
plt.plot(x, y2, label='x^2', color='red')
plt.plot(x, y3, label='x^3', color='green')
plt.plot(x, y4, label='x^4', color='purple')
plt.title('Funções Polinomiais')
plt.xlabel('x')
plt.ylabel('Valores')
plt.legend()
plt.grid()
plt.show()
