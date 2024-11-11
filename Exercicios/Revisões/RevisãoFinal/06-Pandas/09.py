import pandas as pd

df_json = pd.read_json('dados.json')
media_valor = df_json['valor'].mean()
resultado_filtrado = df_json[df_json['valor'] > media_valor]
print(resultado_filtrado)
