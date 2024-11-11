# 5 - Do dataframe 4: renomear todas colunas colocando a primeira letra maiúscula,
#     fazer uma coluna com um desconto de 40% do adiamento salarial e inserir uma
#     outra com o total a receber, fazer um outro dataframe somente com nome,
#     data de aniversario e empresa que trabalha, renomear a coluna empresa que trabalha
#     por Empregador

import pandas as pd

path = r'C:\Users\Aluno\PycharmProjects\IASENAC2024\Exercicios\ExerciciosDaytoDay\Pandas\Arquivos\ExercíciosPandas\04.csv'

df = pd.read_csv(path)

df.columns = df.columns.str.capitalize()

df['Desconto'] = df['Salario'] * 0.40

df['TotalReceber'] = df['Salario'] - df['Desconto']

df_empregador = df[['Nome', 'Aniversario', 'Empresa']].copy()

df_empregador.rename(columns={'Empresa': 'Empregador'}, inplace=True)

print(df)
print(df_empregador)

