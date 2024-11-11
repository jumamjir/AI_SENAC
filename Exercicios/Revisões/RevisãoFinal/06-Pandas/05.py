import pandas as pd

df_excel = pd.read_excel('dados.xlsx')
colunas_nulas = df_excel.columns[df_excel.isnull().any()]
print(colunas_nulas)
