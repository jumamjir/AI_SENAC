notas = []
for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

maior_nota = max(notas)
peso = [1, 1, 1, 2]
media_ponderada = sum(nota * peso[i] for i, nota in enumerate(notas)) / sum(peso)
print(f"A média ponderada é: {media_ponderada:.2f}")
