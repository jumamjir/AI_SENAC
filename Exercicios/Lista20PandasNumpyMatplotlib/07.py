# 7. Leia um arquivo CSV com dados financeiros e utilize 06-Pandas para calcular o
# retorno percentual diário. Use Matplotlib para plotar um gráfico de linhas com o
# retorno acumulado.


import pandas as pd
import matplotlib.pyplot as plt

df7 = pd.read_csv('dados_financeiros.csv')
df7['Retorno'] = df7['Preço'].pct_change()
df7['Retorno Acumulado'] = (1 + df7['Retorno']).cumprod()

df7['Retorno Acumulado'].plot()
plt.title('Retorno Acumulado')
plt.xlabel('Dia')
plt.ylabel('Retorno Acumulado')
plt.show()


