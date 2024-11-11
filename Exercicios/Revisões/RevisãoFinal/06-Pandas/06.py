import pandas as pd

dados_pesquisa = {
    'Categoria': ['A', 'B', 'A', 'C', 'B'],
    'Resposta': [4, 5, 3, 2, 4]
}
df_pesquisa = pd.DataFrame(dados_pesquisa)
media_respostas = df_pesquisa.groupby('Categoria')['Resposta'].mean()
print(media_respostas)
