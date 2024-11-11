# 17. Escreva uma função calcular_correlacao() que receba um DataFrame e duas
# colunas e retorne o coeficiente de correlação entre essas colunas. Trate exceções
# para garantir que ambas as colunas existam e sejam numéricas.


def calcular_correlacao(df, coluna1, coluna2):
    try:
        if coluna1 not in df.columns or coluna2 not in df.columns:
            raise ValueError("Uma ou ambas as colunas não existem no DataFrame.")
        if not pd.api.types.is_numeric_dtype(df[coluna1]) or not pd.api.types.is_numeric_dtype(df[coluna2]):
            raise TypeError("As colunas devem ser numéricas.")
        return df[coluna1].corr(df[coluna2])
    except Exception as e:
        print(f"Erro: {e}")
