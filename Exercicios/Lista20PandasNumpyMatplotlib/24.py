# 24. Crie um DataFrame com valores aleatórios e use NumPy para substituir valores
# abaixo da média por zero. Exiba um gráfico de linha antes e depois da
# substituição.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data24 = np.random.rand(100)
df24 = pd.DataFrame(data24, columns=['Valores'])
media24 = df24['Valores'].mean()

df24['Valores Substituídos'] = df24['Valores'].where(df24['Valores'] >= media24, 0)

plt.plot(df24['Valores'], label='Valores Originais')
plt.plot(df24['Valores Substituídos'], label='Valores Substituídos', linestyle='--')
plt.title('Substituição de Valores Abaixo da Média')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.legend()
plt.show()






