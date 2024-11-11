# 4. Utilize o método.loc[] para selecionar e exibir os dados da segunda linha de um DataFrame.

import pandas as pd


dados= [1,2,3,4,5,6,7,8,9,10]

df = pd.DataFrame({'numeros': dados})
print(df.loc[1])