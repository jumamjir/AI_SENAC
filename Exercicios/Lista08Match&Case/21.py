# 21. Faça um programa que leia o nome de um metal (ouro, prata, bronze) e use
# match/case para exibir a densidade e valor aproximado.

metal = input("Digite o nome do metal (ouro, prata, bronze): ").strip().lower()

match metal:
    case "ouro":
        densidade = "19,32 g/cm³"
        valor = "R$ 300,00 por grama"
    case "prata":
        densidade = "10,49 g/cm³"
        valor = "R$ 5,00 por grama"
    case "bronze":
        densidade = "8,73 g/cm³"
        valor = "R$ 10,00 por quilo"
    case _:
        print("Metal não reconhecido. Tente novamente.")
        exit()

print(f"Densidade do {metal}: {densidade}")
print(f"Valor aproximado do {metal}: {valor}")
