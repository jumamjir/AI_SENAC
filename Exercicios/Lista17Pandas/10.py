# 10. Utilize o método .groupby() para agrupar os dados do DataFrame do exercício 1
# pela coluna cidade e exiba a média dos salários.


import pandas as pd

dados = {'nomes': ['Ana', 'Bruno', 'Carlos'],
         'idades': [23, 25, 30],
         'cidades': ('São Paulo', 'Rio de Janeiro', 'Curitiba'),
         'salario':[3000,3500,4000]
         }

df = pd.DataFrame(dados)
media = df.groupby('cidades')['salario'].mean()
print(media)