# 6. Faça uma função remover_duplicatas() que receba um DataFrame e uma coluna
# como parâmetros e remova as linhas duplicadas com base na coluna fornecida.
# Utilize exceções para tratar erros quando a coluna não existe.

import pandas as pd

def remover_duplicatas(df, coluna):
    try:
        if coluna not in df.columns:
            raise ValueError(f"A coluna '{coluna}' não existe no DataFrame.")

        df_sem_duplicatas = df.drop_duplicates(subset=coluna)
        return df_sem_duplicatas

    except ValueError as e:
        print(e)
        return None



