# 5. Escreva uma função salvar_dataframe() que receba um DataFrame e um nome de
# arquivo, e salve o DataFrame em um arquivo CSV. Trate exceções para erros de
# permissão ou caminhos inválidos.


import pandas as pd


def salvar_dataframe(df, nome_arquivo):
    try:
        df.to_csv(nome_arquivo, index=False)
        print(f"DataFrame salvo com sucesso em '{nome_arquivo}'.")

    except PermissionError:
        print(f"Erro: Permissão negada para salvar em '{nome_arquivo}'.")

    except FileNotFoundError:
        print(f"Erro: O caminho especificado '{nome_arquivo}' é inválido.")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    dados = {
        'nome': ['Alice', 'Bob', 'Charlie', 'David'],
        'idade': [25, 30, 35, 40],
        'cidade': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte']
    }
    df = pd.DataFrame(dados)

    salvar_dataframe(df, 'dados.csv')
