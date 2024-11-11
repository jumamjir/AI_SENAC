# 2. Leia um arquivo CSV com dados de vendas (vendas.csv) usando 06-Pandas, calcule o
# total de vendas por mês e exiba um gráfico de barras com esses dados.

import pandas as pd
import matplotlib.pyplot as plt

df2 = pd.read_csv('vendas.csv')
df2['Data'] = pd.to_datetime(df2['Data'])
df2['Mês'] = df2['Data'].dt.to_period('M')
total_vendas = df2.groupby('Mês')['Vendas'].sum()

total_vendas.plot(kind='bar')
plt.title('Total de Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas')
plt.show()







