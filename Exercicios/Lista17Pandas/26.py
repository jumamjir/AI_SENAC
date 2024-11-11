# 26. Crie um DataFrame com as notas de 3 alunos em 4 disciplinas. Calcule a média
# das notas por aluno e por disciplina.

import pandas as pd

dados = {
    'Aluno': ['Aluno 1', 'Aluno 2', 'Aluno 3'],
    'Matemática': [7.0, 8.5, 6.0],
    'Português': [8.0, 7.5, 9.0],
    'Ciências': [7.5, 6.0, 8.5],
    'História': [6.5, 9.0, 7.0]
}

df = pd.DataFrame(dados)

df['Média por Aluno'] = df[['Matemática', 'Português', 'Ciências', 'História']].mean(axis=1)

media_disciplinas = df[['Matemática', 'Português', 'Ciências', 'História']].mean()

print("Média por Aluno:")
print(df)

print("\nMédia por Disciplina:")
print(media_disciplinas)
