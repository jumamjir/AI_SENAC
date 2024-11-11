# 11. Crie um DataFrame com dados de vendas: produto (A, B, C), quantidade (10, 20,
# 30) e preço (100, 150, 200). Calcule o total de vendas por produto (quantidade *
# preço).
import pandas as pd


dados = {'produto': ['A', 'B', 'C'],
         'quantidade': [10, 20, 30],
         'preco': [100, 150, 200]
         }
df = pd.DataFrame(dados)

df['TotalV'] = df['quantidade'] * df['preco']
print(df)


