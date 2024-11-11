import pandas as pd

dados_vendas = {
    'Produto': ['A', 'B', 'C'],
    'Quantidade': [10, 5, 8],
    'Preço': [20.0, 15.0, 10.0]
}
df_vendas = pd.DataFrame(dados_vendas)

nova_linha = pd.Series({'Produto': 'D', 'Quantidade': 12, 'Preço': 18.0})
df_vendas = df_vendas.append(nova_linha, ignore_index=True)
df_vendas = df_vendas.sort_values(by='Produto')
print(df_vendas)
