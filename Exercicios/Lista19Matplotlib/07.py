# 7. Desenhe uma figura com dois gráficos de linha lado a lado: um com os valores x =
# [1, 2, 3, 4] e y = [1, 4, 9, 16] e outro com x = [1, 2, 3, 4] e y = [1, 8, 27, 64].

import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]

x2 = [1, 2, 3, 4]
y2 = [1, 8, 27, 64]

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].plot(x1, y1, marker='o', color='b')
axs[0].set_title('Gráfico 1: y = x^2')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')

axs[1].plot(x2, y2, marker='o', color='r')
axs[1].set_title('Gráfico 2: y = x^3')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')

plt.tight_layout()
plt.show()

