# 19. Crie um gráfico de linha com múltiplas subplots em uma única figura, mostrando
# diferentes funções matemáticas (seno, cosseno, tangente).

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
seno = np.sin(x)
cosseno = np.cos(x)
tangente = np.tan(x)

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

axs[0].plot(x, seno, color='blue', label='Seno')
axs[0].set_title('Função Seno')
axs[0].set_ylabel('Seno(x)')
axs[0].grid()
axs[0].legend()

axs[1].plot(x, cosseno, color='red', label='Cosseno')
axs[1].set_title('Função Cosseno')
axs[1].set_ylabel('Cosseno(x)')
axs[1].grid()
axs[1].legend()

axs[2].plot(x, tangente, color='green', label='Tangente')
axs[2].set_title('Função Tangente')
axs[2].set_ylabel('Tangente(x)')
axs[2].set_ylim(-10, 10)
axs[2].grid()
axs[2].legend()

plt.tight_layout()
plt.show()
