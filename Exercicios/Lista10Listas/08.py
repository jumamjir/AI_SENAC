# 8. Escreva um programa que leia uma lista de notas de alunos e calcule a média das
# notas.

notas = []

while True:
    nota = input("Digite uma nota (ou '00' para terminar): ")

    if nota == '00':
        break

    if nota.replace('.', '', 1).isdigit() and float(nota) >= 0:
        notas.append(float(nota))
    else:
        print("Por favor, digite um número válido ou 'sair'.")

if notas:
    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi registrada.")
