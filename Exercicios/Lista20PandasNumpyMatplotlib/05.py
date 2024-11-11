# 5. Gere uma matriz 5x5 com números aleatórios entre 0 e 50 usando NumPy. Crie um
# DataFrame a partir dessa matriz e exiba a matriz de correlação entre as colunas
# usando Matplotlib.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data5 = np.random.randint(0, 51, size=(5, 5))
df5 = pd.DataFrame(data5, columns=list('ABCDE'))
correlation = df5.corr()

plt.imshow(correlation, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title('Matriz de Correlação')
plt.show()
