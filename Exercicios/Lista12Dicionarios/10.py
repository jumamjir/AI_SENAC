# 10. Crie um dicionário com nomes de alunos e suas médias e exiba apenas os alunos
# com média acima de 7.

notas_alunos = {
    "Ana": 8.5,
    "Bruno": 6.5,
    "Carla": 9.0,
    "Diego": 7.0,
    "Elena": 5.5
}
alunos_acima_7 = {nome: nota for nome, nota in notas_alunos.items() if nota > 7}
print("Alunos com média acima de 7:", alunos_acima_7)
