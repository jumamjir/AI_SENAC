# 30. Utilize o método .merge() para combinar dois DataFrames com base em uma
# coluna comum e exiba o DataFrame combinado.

import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Nome': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Idade': [25, 30, 22]
})

df_combinado = pd.merge(df1, df2, on='ID', how='inner')

print(df_combinado)
