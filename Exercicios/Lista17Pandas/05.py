# 5. Adicione uma nova coluna ao DataFrame do exercício 1 chamada salário com os
# valores (3000, 3500, 4000). Exiba o DataFrame atualizado.

import pandas as pd

dados = {'nomes': ['Ana', 'Bruno', 'Carlos'],
         'idades': [23, 25, 30],
         'cidades': ('São Paulo', 'Rio de Janeiro', 'Curitiba'),
         'salario':[3000,3500,4000]
         }

df = pd.DataFrame(dados)

print(df)