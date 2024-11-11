# 12. Leia um arquivo CSV com dados de alunos (alunos.csv) e calcule o desvio padrão
# das notas em cada disciplina usando 06-Pandas e NumPy. Exiba um gráfico de barras
# com os desvios padrão.


import pandas as pd
import matplotlib.pyplot as plt

df12 = pd.read_csv('alunos.csv')
desvio_padrao = df12.std()

desvio_padrao.plot(kind='bar')
plt.title('Desvio Padrão das Notas por Disciplina')
plt.xlabel('Disciplinas')
plt.ylabel('Desvio Padrão')
plt.show()




