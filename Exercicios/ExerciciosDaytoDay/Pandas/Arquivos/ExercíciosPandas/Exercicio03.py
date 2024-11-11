# 3 - Do dataframe 2: renomear todas colunas colocando a primeira letra maiúscula,
#     em uma coluna preço de venda será o valor do valor unitário acrescido de 37%,
#     acrescentar uma coluna com o total do preço unitário vezes a quantidade e
#     outra para o total do preço de venda


import pandas as pd

path = r'C:\Users\Aluno\PycharmProjects\IASENAC2024\Exercicios\ExerciciosDaytoDay\Pandas\Arquivos\ExercíciosPandas\02.csv'

df = pd.read_csv(path)

df.columns = df.columns.str.capitalize()
df['PrecoVenda'] = df['Valor_unitario'] * 1.37
print(df)
df['TotalFaturamento'] = df['Valor_unitario'] * df['Quantidade']
print(df)
