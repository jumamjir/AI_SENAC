# 8. Escreva uma função substituir_valores_nulos() que receba um DataFrame e
# substitua os valores nulos por um valor padrão fornecido. Use exceções para
# garantir que o valor padrão é do tipo adequado.

import pandas as pd

def substituir_valores_nulos(df, valor_padrao):
    try:
        if not isinstance(valor_padrao, (int, float, str)):
            raise ValueError(f"O valor padrão deve ser um número ou uma string.")

        df = df.fillna(valor_padrao)
        return df

    except ValueError as e:
        print(e)
        return None


dados = {
        'nome': ['Alice', 'Bob', None, 'David'],
        'idade': [25, None, 35, 40],
        'cidade': ['São Paulo', None, 'São Paulo', 'Belo Horizonte']
    }
df = pd.DataFrame(dados)

resultado = substituir_valores_nulos(df, 'Desconhecido')
print(resultado)

resultado_invalido = substituir_valores_nulos(df, {})
