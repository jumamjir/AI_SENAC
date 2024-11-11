# 14. Carregue um DataFrame com dados de uma pesquisa salarial. Use 06-Pandas para
# agrupar os dados por setor e calcular o salário médio. Exiba um gráfico de barras
# horizontais com os salários médios por setor.

import pandas as pd
import matplotlib.pyplot as plt

df14 = pd.read_csv('pesquisa_salarial.csv')
salario_medio = df14.groupby('Setor')['Salario'].mean()

salario_medio.plot(kind='barh')
plt.title('Salário Médio por Setor')
plt.xlabel('Salário Médio')
plt.ylabel('Setores')
plt.show()




