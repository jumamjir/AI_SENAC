import pandas as pd

caminho1 = r"C:\Users\Aluno\PycharmProjects\IASENAC2024\Exercicios\ExerciciosDaytoDay\Pandas\Arquivos\ExerciciosPandas2\MOCK_DATA-14-10.json"
df1 = pd.read_json(caminho1)

caminho2 = r"C:\Users\Aluno\PycharmProjects\IASENAC2024\Exercicios\ExerciciosDaytoDay\Pandas\Arquivos\ExerciciosPandas2\MOCK_DATA(2) - 14-10.json"
df2 = pd.read_json(caminho2)

print(df1.head(20))
print(df2.head(20))

df_merged = pd.merge(df1, df2, on='id',how='outer')
print(df_merged)


df_merged = pd.merge(df1, df2, on='id',how='inner')
print(df_merged)


df1.fillna(0, inplace=True)
df2.fillna(1, inplace=True)
df_merged = pd.merge(df1, df2, on='id',how='outer')
print(df_merged)