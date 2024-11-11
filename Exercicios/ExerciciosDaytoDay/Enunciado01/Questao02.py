# 02-Tipos de Dados Dinâmicos) Fazer um programa que leia o valor da base e altura de um retângulo
# e retorne se esse retângulo é também quadrado


print("Digite as medidas em centímetros.")
altura = int(input("Digite a medida da altura do retângulo:"))
base = int(input("Digite a medida da base do retângulo:"))

if base == altura:
    print("O retângulo é um quadrado.")
else:
    print("O retângulo não é um quadrado.")
