import pandas as pd

dados = {'nomes': ['Ana', 'Bruno', 'Carlos'],
         'idades': [23, 25, 30],
         'cidades': ('São Paulo', 'Rio de Janeiro', 'Curitiba')
         }

df = pd.DataFrame(dados)

print(df)