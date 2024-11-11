# 14. Escreva uma função plotar_grafico() que receba um DataFrame e duas colunas, e
# exiba um gráfico de linha dessas colunas. Trate exceções para garantir que as
# colunas sejam numéricas e existam no DataFrame.

import matplotlib.pyplot as plt

def plotar_grafico(df, coluna_x, coluna_y):
    try:
        if coluna_x not in df.columns or coluna_y not in df.columns:
            raise ValueError("Uma ou ambas as colunas não existem no DataFrame.")
        if not pd.api.types.is_numeric_dtype(df[coluna_x]) or not pd.api.types.is_numeric_dtype(df[coluna_y]):
            raise TypeError("As colunas devem ser numéricas.")
        plt.plot(df[coluna_x], df[coluna_y])
        plt.xlabel(coluna_x)
        plt.ylabel(coluna_y)
        plt.title('Gráfico de Linha')
        plt.show()
    except Exception as e:
        print(f"Erro: {e}")
