# 13. Adicione uma linha ao DataFrame do exercício 1 com os valores: Diana, 28, Porto
# Alegre, 3800. Exiba o DataFrame atualizado.

import pandas as pd

dados = {'nomes': ['Ana', 'Bruno', 'Carlos','Diana'],
         'idades': [23, 25, 30, 28],
         'cidades': ('São Paulo', 'Rio de Janeiro', 'Curitiba', 'Porto Alegre'),

         }

df = pd.DataFrame(dados)

print(df)