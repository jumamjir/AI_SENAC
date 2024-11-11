# 11. Escreva uma função dividir_colunas() que receba um DataFrame e divida os
# valores de uma coluna numérica por um divisor fornecido pelo usuário. Trate
# exceções para evitar divisão por zero e tipos incompatíveis.


def dividir_colunas(df, coluna, divisor):
    try:
        if coluna not in df.columns:
            raise ValueError(f"A coluna '{coluna}' não existe no DataFrame.")
        if divisor == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        df[coluna] = df[coluna] / divisor
        return df
    except Exception as e:
        print(f"Erro: {e}")
