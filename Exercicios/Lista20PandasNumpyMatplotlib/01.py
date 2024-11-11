# 1. Crie um DataFrame com 100 valores aleatórios entre 0 e 100 usando NumPy.
# Calcule a média e o desvio padrão dos valores e exiba um gráfico de histograma
# usando Matplotlib.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.random.randint(0, 101, size=100)
df1 = pd.DataFrame(data, columns=['Valores'])
media = df1['Valores'].mean()
desvio_padrao = df1['Valores'].std()

plt.hist(df1['Valores'], bins=10, alpha=0.7)
plt.title('Histograma dos Valores')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.show()
