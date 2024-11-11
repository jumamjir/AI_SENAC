# 28. Escreva um programa que solicite um tipo de moeda (dólar, euro, real) e use
# match/case para exibir a cotação aproximada em relação ao real.

moeda = input("Digite o tipo de moeda (dólar, euro, real): ").strip().lower()

match moeda:
    case "dólar":
        cotacao = "Cotação aproximada: R$ 5,00."
    case "euro":
        cotacao = "Cotação aproximada: R$ 5,50."
    case "real":
        cotacao = "Cotação: R$ 1,00."
    case _:
        print("Moeda não reconhecida. Tente novamente.")
        exit()

print(cotacao)
