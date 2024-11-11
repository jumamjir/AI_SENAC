# 4. Utilize 06-Pandas para ler um arquivo Excel (dados.xlsx) com informações de
# temperatura ao longo de um ano. Use NumPy para calcular a média mensal e
# exiba um gráfico de linha com a variação da temperatura ao longo dos meses.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df4 = pd.read_excel('dados.xlsx')
df4['Data'] = pd.to_datetime(df4['Data'])
df4['Mês'] = df4['Data'].dt.to_period('M')
media_temperatura = df4.groupby('Mês')['Temperatura'].mean()

media_temperatura.plot()
plt.title('Média Mensal de Temperatura')
plt.xlabel('Mês')
plt.ylabel('Temperatura Média')
plt.show()
