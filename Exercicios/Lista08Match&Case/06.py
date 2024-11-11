# 6. Solicite ao usuário um número de 1 a 4 e use match/case para exibir uma estação
# do ano (ex: 1 = verão, 2 = outono, etc.).

estacao = int(input("Digite um número de 1 a 4: "))

match estacao:
    case 1:
        print("Verão")
    case 2:
        print("Outuno")
    case 3:
        print("Inverno")
    case 4:
        print("Primavera")