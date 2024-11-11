# 2 - Do dataframe 1: renomear todas colunas colocando a primeira letra maiúscula,
#     acrescentar uma coluna com gratificação de 10% e um total salário com a soma
#     do salario e gratificação

import pandas as pd

path = r'C:\Users\Aluno\PycharmProjects\IASENAC2024\Exercicios\ExerciciosDaytoDay\Pandas\Arquivos\ExercíciosPandas\01.csv'

df = pd.read_csv(path)

print(df)

df.columns = df.columns.str.capitalize()

print(df)

df['Gratificacao'] = df['Salario'] * 0.10

df['TotalSalario'] = df['Salario'] + df['Gratificacao']

print(df)
