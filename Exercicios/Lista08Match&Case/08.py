# 8. Escreva um programa que leia uma nota de 0 a 10 e use match/case para
# categorizar em Ruim, Regular, Bom e Excelente.

nota = float(input("Digite uma nota de 0 a 10: "))

match nota:
    case n if 0 <= n < 4:
        print("Ruim")
    case n if 4 <= n < 7:
        print("Regular")
    case n if 7 <= n < 9:
        print("Bom")
    case n if 9 <= n <= 10:
        print("Excelente")
    case _:
        print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
