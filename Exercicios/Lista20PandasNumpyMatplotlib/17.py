# 17. Leia um arquivo Excel com dados de ações (acoes.xlsx). Calcule a média móvel de
# 10 dias e exiba o gráfico da média móvel sobreposto ao gráfico de preços.

import pandas as pd
import matplotlib.pyplot as plt

df17 = pd.read_excel('acoes.xlsx')
df17['Média Móvel'] = df17['Preço'].rolling(window=10).mean()

plt.plot(df17['Data'], df17['Preço'], label='Preço')
plt.plot(df17['Data'], df17['Média Móvel'], label='Média Móvel de 10 dias')
plt.title('Média Móvel de Preços')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.legend()
plt.show()






