# 7. Ordene o DataFrame do exercício 1 por idade em ordem decrescente e exiba o
# resultado.

import pandas as pd

dados = {'nomes': ['Ana', 'Bruno', 'Carlos'],
         'idades': [23, 25, 30],
         'cidades': ('São Paulo', 'Rio de Janeiro', 'Curitiba')
         }

df = pd.DataFrame(dados)
resultado = df.sort_values(by='idades', ascending=False)
print(resultado)