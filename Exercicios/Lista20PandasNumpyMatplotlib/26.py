# 26. Gere um DataFrame com dados aleatórios e adicione uma coluna com os
# logaritmos dos valores usando NumPy. Exiba gráficos de barras para comparar os
# valores originais e seus logaritmos.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data26 = np.random.rand(10) * 100
df26 = pd.DataFrame(data26, columns=['Valores'])
df26['Logaritmo'] = np.log(df26['Valores'])

df26.plot(kind='bar')
plt.title('Valores e seus Logaritmos')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.legend(['Valores', 'Logaritmo'])
plt.show()











