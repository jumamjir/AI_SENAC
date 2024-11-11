# 14. Substitua os valores nulos em um DataFrame por 0 e exiba o resultado.

import pandas as pd

dados = {'nomes': ['Ana', 'Bruno', 'Carlos'],
         'idades': [23, 25, None],
         'cidades': ('São Paulo', 'Rio de Janeiro', 'Curitiba')
         }

df = pd.DataFrame(dados)
df.fillna(0, inplace=True)

print(df)