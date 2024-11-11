# 3. Faça uma função adicionar_coluna() que receba um DataFrame e adicione uma
# nova coluna com valores fornecidos pelo usuário. Trate exceções para garantir
# que o número de valores corresponde ao número de linhas do DataFrame.

import pandas as pd


def adicionar_coluna(df):
    try:
        valores = input("Digite os valores para a nova coluna, separados por vírgula: ")
        lista_valores = [float(valor.strip()) for valor in valores.split(',')]

        if len(lista_valores) != len(df):
            raise ValueError("O número de valores não corresponde ao número de linhas do DataFrame.")

        df['nova_coluna'] = lista_valores
        print("Coluna adicionada com sucesso!")
        print(df)

    except ValueError as e:
        print("Erro:", e)
    except Exception as e:
        print("Ocorreu um erro:", e)


dados = [10, 20, 30]
df = pd.DataFrame({'numeros': dados})
adicionar_coluna(df)
