# 15. Faça uma função converter_tipo() que receba um DataFrame e uma coluna, e
# converta os valores dessa coluna para um tipo especificado (int, float, str). Trate
# exceções para capturar erros de conversão de tipo.


def converter_tipo(df, coluna, tipo):
    try:
        if coluna not in df.columns:
            raise ValueError(f"A coluna '{coluna}' não existe no DataFrame.")
        df[coluna] = df[coluna].astype(tipo)
        return df
    except Exception as e:
        print(f"Erro: {e}")
