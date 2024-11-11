# 9. Crie uma Series com os valores (10, 20, 30, 40, 50). Exiba a soma, o valor máximo
# e o mínimo da Series.
import pandas as pd


dados= [10, 20, 30, 40, 50]

df = pd.DataFrame({'numeros': dados})

resultado = df.sum()

print(resultado)