# 9. Carregue um DataFrame com dados de uma pesquisa (pesquisa.csv). Calcule a
# proporção de respostas para cada categoria e exiba um gráfico de pizza com
# Matplotlib.


import pandas as pd
import matplotlib.pyplot as plt

df9 = pd.read_csv('pesquisa.csv')
proporcao_respostas = df9['Categoria'].value_counts(normalize=True)

plt.pie(proporcao_respostas, labels=proporcao_respostas.index, autopct='%1.1f%%')
plt.title('Proporção de Respostas por Categoria')
plt.show()




