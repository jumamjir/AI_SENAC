# 24. Desenhe um gráfico de linha duplo para comparar duas séries temporais (A e B)
# em um intervalo de tempo, adicionando rótulos nos eixos e uma legenda.

import numpy as np
import matplotlib.pyplot as plt

tempo = np.arange(0, 10, 0.1)
serie_A = np.sin(tempo)
serie_B = np.cos(tempo)

plt.figure(figsize=(10, 6))
plt.plot(tempo, serie_A, label='Série A (Seno)', color='blue')
plt.plot(tempo, serie_B, label='Série B (Cosseno)', color='orange')
plt.title('Comparação de Séries Temporais')
plt.xlabel('Tempo')
plt.ylabel('Valores')
plt.legend()
plt.grid()
plt.show()
