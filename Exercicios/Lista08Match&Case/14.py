# 14. Faça um programa que leia um número de 1 a 4 e exiba o tipo de quadrilátero
# (quadrado, retângulo, trapézio, etc.) usando match/case.
numero = int(input("Digite um número de 1 a 4 para o tipo de quadrilátero: "))

match numero:
    case 1:
        print("Quadrado")
    case 2:
        print("Retângulo")
    case 3:
        print("Trapézio")
    case 4:
        print("Losango")
    case _:
        print("Número inválido. Por favor, digite um número de 1 a 4.")
