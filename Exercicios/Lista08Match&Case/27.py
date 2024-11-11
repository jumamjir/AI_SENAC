# 27. Faça um programa que leia o nome de uma figura histórica (ex: Newton, Einstein,
# Darwin) e use match/case para exibir uma contribuição científica.

figura = input("Digite o nome de uma figura histórica (Newton, Einstein, Darwin): ").strip().capitalize()

match figura:
    case "Newton":
        contribuicao = "Contribuição: Lei da Gravitação Universal."
    case "Einstein":
        contribuicao = "Contribuição: Teoria da Relatividade."
    case "Darwin":
        contribuicao = "Contribuição: Teoria da Evolução das Espécies."
    case _:
        print("Figura histórica não reconhecida. Tente novamente.")
        exit()

print(contribuicao)

