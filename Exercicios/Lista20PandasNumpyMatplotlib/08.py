# 8. Gere um array de 100 valores aleatórios com distribuição normal usando NumPy.
# Crie um DataFrame e exiba um boxplot para visualizar a distribuição dos dados.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data8 = np.random.normal(loc=0, scale=1, size=100)
df8 = pd.DataFrame(data8, columns=['Valores'])

plt.boxplot(df8['Valores'])
plt.title('Boxplot de Valores')
plt.ylabel('Valores')
plt.show()


