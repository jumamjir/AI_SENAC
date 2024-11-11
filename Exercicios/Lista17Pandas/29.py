# 29. Crie um DataFrame com 5 colunas (A, B, C, D, E) e 10 linhas. Calcule a soma de
# cada linha e adicione o resultado como uma nova coluna Soma.

import pandas as pd
import random

data = {
    'A': [random.randint(1, 10) for _ in range(10)],
    'B': [random.randint(1, 10) for _ in range(10)],
    'C': [random.randint(1, 10) for _ in range(10)],
    'D': [random.randint(1, 10) for _ in range(10)],
    'E': [random.randint(1, 10) for _ in range(10)],
}
df = pd.DataFrame(data)

df['Soma'] = df.sum(axis=1)

print(df)
