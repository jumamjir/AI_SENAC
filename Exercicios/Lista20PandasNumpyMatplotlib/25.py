# 25. Leia um arquivo CSV com dados de consumo energético e exiba um gráfico de
# linha com a variação do consumo ao longo do tempo. Use Matplotlib para
# adicionar uma linha de tendência calculada com NumPy.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df25 = pd.read_csv('consumo_energetico.csv')
df25['Data'] = pd.to_datetime(df25['Data'])

plt.plot(df25['Data'], df25['Consumo'], label='Consumo')
z = np.polyfit(df25.index, df25['Consumo'], 1)
p = np.poly1d(z)
plt.plot(df25['Data'], p(df25.index), label='Linha de Tendência', linestyle='--')

plt.title('Variação do Consumo Energético ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Consumo')
plt.legend()
plt.show()








