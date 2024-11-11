# 19. Remova as linhas duplicadas em um DataFrame com base na coluna nome e
# exiba o DataFrame atualizado.

import pandas as pd

dados = {
    'nomes': ['Ana', 'Bruno', 'Carlos', 'Ana'],
    'idades': [23, 25, 30, 23],
    'cidades': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'São Paulo'],
    'salario': [3000, 3500, 4000, 3000]
}

df = pd.DataFrame(dados)

df_atualizado = df.drop_duplicates(subset='nomes')

print(df_atualizado)
