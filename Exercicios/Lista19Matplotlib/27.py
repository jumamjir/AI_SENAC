# 27. Desenhe um gráfico de radar para comparar as pontuações de um jogador em
# cinco habilidades diferentes.

import numpy as np
import matplotlib.pyplot as plt
from math import pi

habilidades = ['Habilidade A', 'Habilidade B', 'Habilidade C', 'Habilidade D', 'Habilidade E']
pontuacoes = [3, 4, 2, 5, 4]

N = len(habilidades)
angles = [n / float(N) * 2 * pi for n in range(N)]
pontuacoes += pontuacoes[:1]
angles += angles[:1]

plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)
plt.xticks(angles[:-1], habilidades)
ax.plot(angles, pontuacoes, linewidth=1, linestyle='solid', label='Jogador')
ax.fill(angles, pontuacoes, 'b', alpha=0.1)
plt.title('Comparação de Habilidades')
plt.legend()
plt.show()
