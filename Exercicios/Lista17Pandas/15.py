# 15. Renomeie as colunas nome e idade do DataFrame do exercício 1 para Nome
# Completo e Idade Anos, respectivamente. Exiba o DataFrame atualizado.

import pandas as pd

dados = {'Nome Completo': ['Ana Maria Braga', 'Bruno e Marrone', 'Carlos Alexandre'],
         'Idade Anos': [2001, 1999, 1994],
         'cidades': ('São Paulo', 'Rio de Janeiro', 'Curitiba')
         }

df = pd.DataFrame(dados)

print(df)