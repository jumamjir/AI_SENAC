# 18. Crie um DataFrame com dados de funcionários: nome (Pedro, Maria), setor (TI,
# RH), e salário (5000, 4500). Agrupe os dados por setor e calcule a média salarial
# por setor.

import pandas as pd

dados = {'nome': ['Pedro', 'Maria'],
         'setor': ['TI', 'RH'],
         'salario':[5000,4500]
         }
df = pd.DataFrame(dados)
resultado = df.groupby('setor')['salario'].mean()
print(resultado)