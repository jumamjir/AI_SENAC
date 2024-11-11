# 13. Gere um DataFrame com valores aleatórios e adicione uma coluna com os valores
# de sua raiz quadrada usando NumPy. Exiba um gráfico de linha com as colunas
# originais e a nova coluna.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data13 = np.random.rand(10, 1) * 100
df13 = pd.DataFrame(data13, columns=['Valores'])
df13['Raiz Quadrada'] = np.sqrt(df13['Valores'])

plt.plot(df13['Valores'], label='Valores')
plt.plot(df13['Raiz Quadrada'], label='Raiz Quadrada')
plt.title('Valores e Raiz Quadrada')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.legend()
plt.show()




