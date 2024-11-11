# 16. Crie uma função remover_linhas_vazias() que receba um DataFrame e remova
# todas as linhas que contenham valores nulos. Use tratamento de exceção para
# garantir que o DataFrame não esteja vazio após a remoção.


def remover_linhas_vazias(df):
    try:
        df = df.dropna()
        if df.empty:
            raise ValueError("O DataFrame está vazio após a remoção de linhas vazias.")
        return df
    except Exception as e:
        print(f"Erro: {e}")
