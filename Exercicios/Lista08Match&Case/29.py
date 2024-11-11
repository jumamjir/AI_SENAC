# 29. Solicite ao usuário um tipo de bebida (água, suco, refrigerante) e use match/case
# para exibir a quantidade média de açúcar.

bebida = input("Digite o tipo de bebida (água, suco, refrigerante): ").strip().lower()

match bebida:
    case "água":
        acucar = "Água não contém açúcar."
    case "suco":
        acucar = "Quantidade média de açúcar: 10g por 100ml."
    case "refrigerante":
        acucar = "Quantidade média de açúcar: 40g por 100ml."
    case _:
        print("Bebida não reconhecida. Tente novamente.")
        exit()

print(acucar)
