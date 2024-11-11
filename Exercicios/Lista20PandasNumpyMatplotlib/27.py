# 27. Carregue um DataFrame com dados de produção de uma fábrica. Use 06-Pandas
# para calcular a produção média mensal e exiba um gráfico de barras com a
# variação da produção ao longo dos meses.


import pandas as pd
import matplotlib.pyplot as plt

df27 = pd.read_csv('producao_fabrica.csv')
df27['Data'] = pd.to_datetime(df27['Data'])
df27['Mês'] = df27['Data'].dt.to_period('M')
producao_media = df27.groupby('Mês')['Produção'].mean()

producao_media.plot(kind='bar')
plt.title('Produção Média Mensal')
plt.xlabel('Mês')
plt.ylabel('Produção Média')
plt.show()










