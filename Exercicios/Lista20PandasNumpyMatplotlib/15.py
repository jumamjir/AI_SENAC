# 15. Crie um DataFrame com dados de temperatura de várias cidades e use NumPy
# para calcular o desvio padrão por cidade. Exiba um gráfico de linha com as
# temperaturas e sombreie o desvio padrão.

import pandas as pd
import matplotlib.pyplot as plt

df15 = pd.read_csv('temperaturas.csv')
desvio_padrao_cidade = df15.groupby('Cidade')['Temperatura'].std()

plt.plot(df15['Cidade'], df15['Temperatura'])
plt.fill_between(df15['Cidade'], df15['Temperatura'] - desvio_padrao_cidade,
                 df15['Temperatura'] + desvio_padrao_cidade, alpha=0.2)
plt.title('Temperaturas por Cidade com Desvio Padrão')
plt.xlabel('Cidade')
plt.ylabel('Temperatura')
plt.show()




