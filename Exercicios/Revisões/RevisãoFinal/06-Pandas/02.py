import pandas as pd

df_produtos = pd.read_csv('produtos.csv')
df_produtos['Desconto'] = df_produtos['Preço'] * 0.10
print(df_produtos)
