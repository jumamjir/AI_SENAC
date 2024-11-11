# Exercício 8: Média de Notas e Status dos Alunos
# • Enunciado: Criar um programa com uma lista de 100 posições para
# armazenar a média de duas notas de 100 alunos. Verificar o status de cada
# aluno (Aprovado, Recuperação ou Reprovado) e mostrar no final todos os
# alunos com suas notas, médias e status.
# o Status:
# ▪ Aprovado: média maior ou igual a 7
# ▪ Recuperação: média menor que 7 e maior ou igual a 6
# ▪ Reprovado: média menor que 6
# • Estruturas Usar: for, if/elif/else, input, print

media_lista = []
status_lista = []

for i in range(100):
    print(f"Aluno {i + 1}:")

    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))

    media = (n1 + n2) / 2
    media_lista.append(media)

    if media >= 7:
        status = "Aprovado"
    elif media >= 6:
        status = "Recuperação"
    else:
        status = "Reprovado"

    status_lista.append(status)

print("\nResultados:")
for i in range(100):
    print(f"Aluno {i + 1}: Média = {media_lista[i]:.2f}, Status = {status_lista[i]}")
