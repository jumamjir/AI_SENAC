# 1. Crie um dicionário com 3 alunos e suas notas. Exiba a média das notas dos
# alunos.
alunos = {
    "João": 7.5,
    "Maria": 8.0,
    "Carlos": 6.5
}
media = sum(alunos.values()) / len(alunos)
print(f"Média das notas: {media:.2f}")
