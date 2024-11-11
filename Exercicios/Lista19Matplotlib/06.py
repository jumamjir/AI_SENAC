# 6. Crie um gráfico de linha com as funções seno e cosseno no intervalo de 0 a 2π.
# Adicione uma legenda para identificar cada função.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)

y_seno = np.sin(x)
y_cosseno = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y_seno, label='Seno', color='blue')
plt.plot(x, y_cosseno, label='Cosseno', color='orange')

plt.title('Gráfico das Funções Seno e Cosseno')
plt.xlabel('Ângulo (radianos)')
plt.ylabel('Valor')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.legend()

plt.show()


