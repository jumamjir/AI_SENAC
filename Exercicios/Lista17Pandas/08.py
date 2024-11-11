# 8. Remova a coluna cidade do DataFrame do exercício 1 e exiba o DataFrame
# atualizado.

import pandas as pd

dados = {'nomes': ['Ana', 'Bruno', 'Carlos'],
         'idades': [23, 25, 30],
         'cidades': ('São Paulo', 'Rio de Janeiro', 'Curitiba')
         }

df = pd.DataFrame(dados)
resultado = df.drop(columns=['cidades'])
print(resultado)