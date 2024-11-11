import pandas as pd

df_duplicados = pd.read_csv('dados.csv')
df_sem_duplicados = df_duplicados.drop_duplicates(subset='coluna_especifica')
print(df_sem_duplicados)
