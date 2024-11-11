# 27. Utilize o método .describe() em um DataFrame para exibir as estatísticas

import pandas as pd

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 6, 7, 8, 9],
    'C': ['foo', 'bar', 'foo', 'bar', 'foo']
}
df = pd.DataFrame(data)

estatisticas = df.describe()

print(estatisticas)
