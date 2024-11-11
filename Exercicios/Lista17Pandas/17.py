# 17. Utilize o método .apply() para adicionar 10% ao salário de cada pessoa no
# DataFrame do exercício 1. Exiba o DataFrame atualizado.

import pandas as pd

dados = {'nomes': ['Ana', 'Bruno', 'Carlos'],
         'idades': [23, 25, 30],
         'cidades': ('São Paulo', 'Rio de Janeiro', 'Curitiba'),
         'salario':[3000,3500,4000]
         }

df = pd.DataFrame(dados)
df['salario'] = df['salario'].apply(lambda x: x * 1.1)
print(df)