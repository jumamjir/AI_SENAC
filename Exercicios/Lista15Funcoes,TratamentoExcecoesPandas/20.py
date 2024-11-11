# 20. Escreva uma função extrair_amostra() que receba um DataFrame e um número n,
# e retorne uma amostra aleatória de n linhas. Utilize exceções para garantir que n
# seja menor ou igual ao número de linhas do DataFrame.

def extrair_amostra(df, n):
    try:
        if n > len(df):
            raise ValueError("O valor de n deve ser menor ou igual ao número de linhas do DataFrame.")
        return df.sample(n)
    except Exception as e:
        print(f"Erro: {e}")
