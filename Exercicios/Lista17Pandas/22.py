# 22. Faça um merge entre dois DataFrames, um contendo nomes e idades, e outro
# contendo nomes e salários. Exiba o DataFrame resultante.
import pandas as pd

dados = {
    'nomes': ['Ana', 'Bruno', 'Carlos'],
    'idades': [23, 25, 30]
}
df = pd.DataFrame(dados)

dados1 = {
    'nomes': ['Joao', 'Pedro', 'Amanda'],
    'salario': [4300, 2700, 5000]
}
fd = pd.DataFrame(dados1)

total = pd.merge(df, fd, on='nomes', how='outer')

print(total)



