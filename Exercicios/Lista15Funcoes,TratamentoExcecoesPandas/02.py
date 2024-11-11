# 2. Escreva uma função calcular_media() que receba um DataFrame e uma coluna
# como parâmetros e retorne a média dos valores dessa coluna. Utilize exceções
# para verificar se a coluna existe.

import pandas as pd


def calcular_media(df, coluna):
    try:
        if coluna not in df.columns:
            raise ValueError(f"A coluna '{coluna}' não existe no DataFrame.")

        media = df[coluna].mean()
        return media

    except ValueError as e:
        print("Erro:", e)


dados = [10, 2, 5, 8]
df = pd.DataFrame({'numeros': dados})
media_numeros = calcular_media(df, 'numeros')

if media_numeros is not None:
    print("A média é:", media_numeros)
