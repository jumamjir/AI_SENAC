# 28. Crie um DataFrame com dados de vendas de produtos ao longo de um ano. Use
# NumPy para calcular o crescimento percentual mês a mês e exiba um gráfico de
# linha.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df28 = pd.read_csv('vendas_anual.csv')
df28['Crescimento Percentual'] = df28['Vendas'].pct_change() * 100

plt.plot(df28['Mês'], df28['Crescimento Percentual'])
plt.title('Crescimento Percentual Mês a Mês')
plt.xlabel('Mês')
plt.ylabel('Crescimento Percentual (%)')
plt.show()










