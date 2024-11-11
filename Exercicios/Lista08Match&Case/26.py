# 26. Crie um programa que solicite uma categoria de alimento (fruta, legume, carne) e
# use match/case para exibir exemplos de alimentos.

categoria = input("Digite uma categoria de alimento (fruta, legume, carne): ").strip().lower()

match categoria:
    case "fruta":
        exemplos = "Exemplos: maçã, banana, laranja."
    case "legume":
        exemplos = "Exemplos: cenoura, brócolis, batata."
    case "carne":
        exemplos = "Exemplos: frango, boi, porco."
    case _:
        print("Categoria não reconhecida. Tente novamente.")
        exit()

print(exemplos)

