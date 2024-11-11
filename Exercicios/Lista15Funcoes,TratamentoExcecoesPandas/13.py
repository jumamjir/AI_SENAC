# 13. Crie uma função agrupar_por_coluna() que receba um DataFrame, uma coluna
# para agrupar e outra para calcular a soma. Utilize exceções para verificar se as
# colunas existem e se possuem tipos compatíveis para agregação.

def agrupar_por_coluna(df, coluna_agrupamento, coluna_soma):
    try:
        if coluna_agrupamento not in df.columns or coluna_soma not in df.columns:
            raise ValueError("Uma ou ambas as colunas não existem no DataFrame.")
        return df.groupby(coluna_agrupamento)[coluna_soma].sum()
    except Exception as e:
        print(f"Erro: {e}")
