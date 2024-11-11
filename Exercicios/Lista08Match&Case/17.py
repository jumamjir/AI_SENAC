# 17. Faça um programa que leia um número de 1 a 10 e use match/case para exibir o
# número por extenso (ex: 1 = "um", 2 = "dois").
numero = int(input("Digite um número de 1 a 10: "))

match numero:
    case 1:
        print("Um")
    case 2:
        print("Dois")
    case 3:
        print("Três")
    case 4:
        print("Quatro")
    case 5:
        print("Cinco")
    case 6:
        print("Seis")
    case 7:
        print("Sete")
    case 8:
        print("Oito")
    case 9:
        print("Nove")
    case 10:
        print("Dez")
    case _:
        print("Número inválido. Por favor, digite um número de 1 a 10.")
