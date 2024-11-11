# 23. Utilize o método .pivot_table() para criar uma tabela dinâmica a partir de um
# DataFrame que contém dados de vendas por produto e região. Exiba a soma das
# vendas por produto e região.

import pandas as pd

dados = {
    'produto': ['Produto A', 'Produto B', 'Produto A', 'Produto B', 'Produto C', 'Produto A'],
    'regiao': ['Norte', 'Norte', 'Sul', 'Sul', 'Norte', 'Sul'],
    'vendas': [100, 150, 200, 250, 300, 400]
}

df = pd.DataFrame(dados)

tabela_dinamica = df.pivot_table(values='vendas', index='produto', columns='regiao', aggfunc='sum', fill_value=0)

print(tabela_dinamica)
