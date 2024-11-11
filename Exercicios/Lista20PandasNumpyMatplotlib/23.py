# 23. Carregue um arquivo CSV com dados de vendas e calcule o total de vendas por
# produto usando 06-Pandas. Exiba um gráfico de pizza para visualizar a participação
# de cada produto nas vendas totais.


import pandas as pd
import matplotlib.pyplot as plt

df23 = pd.read_csv('vendas.csv')
total_vendas_produto = df23.groupby('Produto')['Vendas'].sum()

plt.pie(total_vendas_produto, labels=total_vendas_produto.index, autopct='%1.1f%%')
plt.title('Participação de Cada Produto nas Vendas Totais')
plt.show()










