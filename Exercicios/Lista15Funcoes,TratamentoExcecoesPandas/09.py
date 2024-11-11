# 9. Faça uma função ordenar_dataframe() que receba um DataFrame e uma coluna e
# retorne o DataFrame ordenado pela coluna especificada. Trate exceções para
# verificar se a coluna é válida.


import pandas as pd


def ordenar_dataframe(df, coluna):
    try:
        if coluna not in df.columns:
            raise ValueError(f"A coluna {coluna}, não existe no DataFrame.")

        df_ordenado = df.sort_values(by=coluna)
        return df_ordenado

    except ValueError as e:
        print(e)

dados = {
        'nome': ['Alice', 'Bob', 'Charlie', 'David'],
        'idade': [25, 30, 35, 20],
        'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
    }

df = pd.DataFrame(dados)

resultado = ordenar_dataframe(df, 'idade')
print(resultado)


