# 6- Filtre e exiba as linhas do DataFrame onde a idade é maior que 25.

import pandas as pd

dados = {'nomes': ['Ana', 'Bruno', 'Carlos'],
         'idades': [23, 25, 30],
         'cidades': ('São Paulo', 'Rio de Janeiro', 'Curitiba'),
         'salario':[3000,3500,4000]
         }

df = pd.DataFrame(dados)

resultado = df.query('idades > 25')

print(resultado)