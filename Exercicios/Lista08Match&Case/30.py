# 30. Crie um programa que solicite uma função matemática (log, exp, sqrt) e um
# número, usando match/case para calcular o resultado com a função math.

import math

funcao = input("Digite uma função matemática (log, exp, sqrt): ").strip().lower()
numero = float(input("Digite um número: "))

match funcao:
    case "log":
        resultado = math.log(numero)
    case "exp":
        resultado = math.exp(numero)
    case "sqrt":
        resultado = math.sqrt(numero)
    case _:
        print("Função não reconhecida. Tente novamente.")
        exit()

print(f"O resultado é: {resultado}")
