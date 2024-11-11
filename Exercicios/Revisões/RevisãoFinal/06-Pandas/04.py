import pandas as pd

dados_vendas = {
    'Produto': ['A', 'B', 'C'],
    'Quantidade': [10, 5, 8],
    'Preço': [20.0, 15.0, 10.0]
}
df_vendas = pd.DataFrame(dados_vendas)
df_vendas['Preço_Acrescido'] = df_vendas['Preço'] * 1.15
print(df_vendas)
