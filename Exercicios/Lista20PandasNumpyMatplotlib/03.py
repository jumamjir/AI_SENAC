# 3. Crie um DataFrame com 3 colunas (A, B, C) com 50 valores aleatórios. Use
# Matplotlib para exibir um gráfico de dispersão entre as colunas A e B, colorindo os
# pontos com base nos valores da coluna C.




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data3 = np.random.rand(50, 3)
df3 = pd.DataFrame(data3, columns=['A', 'B', 'C'])

plt.scatter(df3['A'], df3['B'], c=df3['C'], cmap='viridis')
plt.colorbar(label='Valores da Coluna C')
plt.xlabel('Coluna A')
plt.ylabel('Coluna B')
plt.title('Gráfico de Dispersão entre A e B')
plt.show()
