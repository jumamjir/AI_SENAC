# 1. Crie uma função ler_csv() que leia um arquivo CSV e retorne um DataFrame.
# Utilize tratamento de exceção para lidar com arquivos inexistentes ou erros de
# leitura.

import pandas as pd

def ler_csv():
    try:
        df = pd.read_csv('Dados.csv')
        return df
    except FileNotFoundError:
        print("Erro: O arquivo 'Dados.csv' não foi encontrado.")
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo está vazio.")
    except pd.errors.ParserError:
        print("Erro: Problema ao ler o arquivo. O formato pode estar incorreto.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

dataframe = ler_csv()
if dataframe is not None:
    print(dataframe)