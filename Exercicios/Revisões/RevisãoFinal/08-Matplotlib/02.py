import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
seno = np.sin(x)
cosseno = np.cos(x)
tangente = np.tan(x)

plt.plot(x, seno, label='Seno')
plt.plot(x, cosseno, label='Cosseno')
plt.plot(x, tangente, label='Tangente')
plt.ylim(-10, 10)
plt.title('Gráfico de Linhas: Seno, Cosseno e Tangente')
plt.xlabel('X')
plt.ylabel('Valor')
plt.legend()
plt.grid()
plt.show()
