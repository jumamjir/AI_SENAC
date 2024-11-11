# 4 - Do dataframe 3: renomear todas colunas colocando a primeira letra maiúscula,
#     agrupar por marca de veiculo

import pandas as pd

path = r'C:\Users\Aluno\PycharmProjects\IASENAC2024\Exercicios\ExerciciosDaytoDay\Pandas\Arquivos\ExercíciosPandas\03.csv'

df = pd.read_csv(path)

df.columns = df.columns.str.capitalize()
df.groupby(by=['Marca_veiculo'])
print(df)
