# 18. Faça uma função mesclar_dataframes() que receba dois DataFrames e uma
# coluna comum para realizar um merge. Utilize exceções para tratar
# incompatibilidades de tipos e colunas inexistentes.

def mesclar_dataframes(df1, df2, coluna_comum):
    try:
        if coluna_comum not in df1.columns or coluna_comum not in df2.columns:
            raise ValueError("A coluna comum não existe em um dos DataFrames.")
        return pd.merge(df1, df2, on=coluna_comum)
    except Exception as e:
        print(f"Erro: {e}")
