# 8. Crie um programa que leia várias notas de alunos e ignore notas menores que zero
# (continue).

while True:
    nota = float(input("Digite sua nota:(digite '-0' para sair):"))

    if nota < 0:
        continue
    elif nota == -0:
        break
    else:
        print(nota)