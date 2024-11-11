# 11. Faça um programa que leia um número de 1 a 5 e exiba um símbolo matemático
# (+, -, *, /, ^) correspondente usando match/case.

numero = int(input("Digite um número de 1 a 5: "))

match numero:
    case 1:
        print("Símbolo: +")
    case 2:
        print("Símbolo: -")
    case 3:
        print("Símbolo: *")
    case 4:
        print("Símbolo: /")
    case 5:
        print("Símbolo: ^")
    case _:
        print("Número inválido. Por favor, digite um número de 1 a 5.")
