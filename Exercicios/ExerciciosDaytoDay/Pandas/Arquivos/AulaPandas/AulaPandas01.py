import pandas as pd

caminho = r'C:\Users\Aluno\PycharmProjects\IASENAC2024\Arquivos\Dados.csv'

df = pd.read_csv(caminho)

print(df.describe())
# print(df.info())
# print(df.head(15))
# print(df.tail(10))
