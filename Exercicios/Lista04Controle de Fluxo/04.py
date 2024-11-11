# 4.Solicite a nota de um aluno e exiba se ele foi aprovado (nota ≥ 7), está em
# recuperação (5 ≤ nota < 7) ou reprovado (nota < 5).


nota = float(input("Digite sua nota:"))


if nota >= 7:
    print("Aprovado")
elif nota >=5:
    print("Recuperação")
elif nota < 5:
    print("Reprovado")
else:
    print("Inválido")
