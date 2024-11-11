# 3. Faça um programa que leia o dia da semana (1 a 7) e use match/case para exibir o
# nome do dia correspondente. Utilize while para pedir a entrada novamente caso o
# número seja inválido.

while True:
    numero = int(input("Digite um número de 1 a 7: "))
    match numero:
        case 1:
            print("Domingo")
            break
        case 2:
            print("Segunda-feira")
            break
        case 3:
            print("Terça-feira")
            break
        case 4:
            print("Quarta-feira")
            break
        case 5:
            print("Quinta-feira")
            break
        case 6:
            print("Sexta-feira")
            break
        case 7:
            print("Sábado")
            break
        case _:
            print("Número inválido. Por favor, digite um número de 1 a 7.")
            continue