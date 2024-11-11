# 7. Crie uma função calcular_desvio_padrao() que receba um DataFrame e uma
# coluna e retorne o desvio padrão dos valores. Utilize tratamento de exceções para
# verificar se a coluna contém valores numéricos.

import pandas as pd


def calcular_desvio_padrao(df, coluna):
    try:
        if coluna not in df.columns:
            raise ValueError(f"A coluna {coluna} não existe no DataFrame.")

        desvio_padrao = df[coluna].std()

        return desvio_padrao

    except ValueError as e:
        print(e)

dados = {
        'nome': ['Alice', 'Bob', 'Charlie', 'David'],
        'idade': [25, 30, 35, 40],
        'cidade': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte']
    }
df = pd.DataFrame(dados)
a = calcular_desvio_padrao(df,'idade')
print(a)
