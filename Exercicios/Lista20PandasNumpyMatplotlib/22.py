# 22. Leia um DataFrame com dados de notas de estudantes e utilize 06-Pandas para
# calcular a nota média por disciplina. Exiba um gráfico de barras com a média de
# cada disciplina.


import pandas as pd
import matplotlib.pyplot as plt

df22 = pd.read_csv('notas_estudantes.csv')
media_disciplinas = df22.mean()

media_disciplinas.plot(kind='bar')
plt.title('Nota Média por Disciplina')
plt.xlabel('Disciplinas')
plt.ylabel('Nota Média')
plt.show()












