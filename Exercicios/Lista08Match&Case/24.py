# 24. Faça um programa que leia um valor e um tipo de conversão (metros para
# centímetros, quilogramas para gramas) e use match/case para converter o valor.

valor = float(input("Digite um valor: "))
conversao = input("Digite o tipo de conversão (metros para centímetros, quilogramas para gramas): ").strip().lower()

match conversao:
    case "metros para centímetros":
        resultado = valor * 100
    case "quilogramas para gramas":
        resultado = valor * 1000
    case _:
        print("Conversão não reconhecida. Tente novamente.")
        exit()

print(f"Resultado da conversão: {resultado}")
