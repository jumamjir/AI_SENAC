# 29. Leia um arquivo Excel com dados financeiros e use 06-Pandas para calcular os
# indicadores de desempenho (P/L, ROE). Exiba um gráfico de barras para comparar
# os indicadores entre diferentes empresas.


import pandas as pd
import matplotlib.pyplot as plt

df29 = pd.read_excel('dados_financeiros.xlsx')
df29['P/L'] = df29['Lucro'] / df29['Valor de Mercado']
df29['ROE'] = df29['Lucro'] / df29['Patrimonio']

df29[['Empresa', 'P/L', 'ROE']].set_index('Empresa').plot(kind='bar')
plt.title('Indicadores de Desempenho por Empresa')
plt.ylabel('Indicador')
plt.show()















