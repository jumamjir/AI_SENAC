# 20. Crie um DataFrame com 10 linhas e 3 colunas com valores aleatórios entre 0 e
# 100. Exiba a matriz de correlação das colunas.

import pandas as pd
import random

dados = {
    'Coluna1': [random.randint(0, 100) for _ in range(10)],
    'Coluna2': [random.randint(0, 100) for _ in range(10)],
    'Coluna3': [random.randint(0, 100) for _ in range(10)],
}

df = pd.DataFrame(dados)

print(df)

matriz = df.corr()
print("\nMatriz de Correlação:")
print(matriz)
