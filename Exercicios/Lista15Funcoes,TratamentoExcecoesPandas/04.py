# 4. Crie uma função filtrar_dados() que receba um DataFrame, uma coluna e um
# valor, e retorne um novo DataFrame filtrado. Utilize exceções para tratar erros caso
# a coluna não exista.

import pandas as pd


def filtrar_dados(df, coluna, valor):
    try:
        if coluna not in df.columns:
            raise ValueError(f"A coluna '{coluna}' não existe no DataFrame.")

        novo_df = df[df[coluna] == valor]
        return novo_df

    except ValueError as e:
        print(e)
        return None


if __name__ == "__main__":
    dados = {
        'nome': ['Alice', 'Bob', 'Charlie', 'David'],
        'idade': [25, 30, 35, 40],
        'cidade': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte']
    }
    df = pd.DataFrame(dados)

    resultado = filtrar_dados(df, 'cidade', 'São Paulo')
    print(resultado)

    resultado_invalido = filtrar_dados(df, 'profissao', 'Engenheiro')
