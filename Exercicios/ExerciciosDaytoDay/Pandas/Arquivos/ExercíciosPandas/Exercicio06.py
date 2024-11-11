# 6 - Do dataframe 5: renomear todas colunas colocando a primeira letra maiúscula,
#     acrescentar 5% no limite do cartão, acrescentar uma coluna para país.

import pandas as pd

path = r'C:\Users\Aluno\PycharmProjects\IASENAC2024\Exercicios\ExerciciosDaytoDay\Pandas\Arquivos\ExercíciosPandas\05.csv'

df = pd.read_csv(path)

df.columns = df.columns.str.capitalize()
print(df)
df['Limite'] = df['Limite'] * 1.05
df['Pais'] = 'Brasil'
print(df)
