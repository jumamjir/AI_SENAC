import pandas as pd

dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'Nota': [8.5, 7.0, 6.5, 9.0, 5.5],
    'Idade': [22, 19, 23, 21, 18]
}
df_alunos = pd.DataFrame(dados)
alunos_maior_20 = df_alunos[df_alunos['Idade'] > 20]
print(alunos_maior_20)
