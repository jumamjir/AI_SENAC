# 10. Crie uma função buscar_valores() que receba um DataFrame, uma coluna e um
# valor para buscar todas as ocorrências desse valor na coluna. Use tratamento de
# exceções para garantir que a busca seja feita em colunas válidas.


import pandas as pd

def buscar_valores(df, coluna, valor):
    try:
        if coluna not in df.columns:
            raise ValueError(f"A coluna '{coluna}' não existe no DataFrame.")
        return df[df[coluna] == valor]
    except Exception as e:
        print(f"Erro: {e}")
