# 1 - Utilizar nos dataframesr: o índex, dtype, shape, size, ndmi, empty, escolha um deles para usar o
# transpose ou T, axes, head, tail drop(somente um), describe, loc, iloc, at, iat, sort_values.

import pandas as pd

path = r'C:\Users\Aluno\PycharmProjects\IASENAC2024\Exercicios\ExerciciosDaytoDay\Pandas\Arquivos\ExercíciosPandas\01.csv'

df = pd.read_csv(path)
print(df)

print("DataFrame:")
print(df)

print("Índex:")
print(df.index)

print("Dtype:")
print(df.dtypes)

print("Shape:")
print(df.shape)

print("Size:")
print(df.size)

print("ndim:")
print(df.ndim)

print("Empty:")
print(df.empty)

print("Transposed:")
print(df.T)

print("Axes:")
print(df.axes)

print("Head:")
print(df.head())

print("Tail:")
print(df.tail())

print("Usando drop:")
df_drop = df.drop(index=0)
print(df_drop)

print("Describe:")
print(df.describe())

print("Usando loc para acessar a primeira linha:")
print(df.loc[0])

print("Usando iloc para acessar a primeira linha:")
print(df.iloc[0])

print("Usando at para acessar (linha 0, coluna 0):")
print(df.at[0, df.columns[0]])

print("Usando iat para acessar (linha 0, coluna 0):")
print(df.iat[0, 0])

print("Ordenado pela primeira coluna:")
df_sorted = df.sort_values(by=df.columns[0])
print(df_sorted)
