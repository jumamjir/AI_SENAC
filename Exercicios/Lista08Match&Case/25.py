# 25. Escreva um programa que solicite uma cor (vermelho, azul, verde) e use
# match/case para exibir a combinação de cores primárias que formam essa cor.

cor = input("Digite uma cor (vermelho, azul, verde): ").strip().lower()

match cor:
    case "vermelho":
        combinacao = "Vermelho é uma cor primária."
    case "azul":
        combinacao = "Azul é uma cor primária."
    case "verde":
        combinacao = "Verde é formado pela combinação de azul e amarelo."
    case _:
        print("Cor não reconhecida. Tente novamente.")
        exit()

print(combinacao)
