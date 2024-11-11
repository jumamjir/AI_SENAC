import pandas as pd

dados_vendas = {
    'Produto': ['A', 'B', 'C'],
    'Quantidade': [10, 5, 8],
    'Preço': [20.0, 15.0, 10.0]
}
df_vendas = pd.DataFrame(dados_vendas)
df_vendas['Total'] = df_vendas['Quantidade'] * df_vendas['Preço']
print(df_vendas)
