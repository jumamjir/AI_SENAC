# 7. Faça um programa que leia uma letra (a, e, i, o, u) e use match/case para indicar se
# é uma vogal ou exiba uma mensagem de erro.

vogal = input("Digite uma letra (a, e, i, o, u): ").strip().lower()

match vogal:
    case 'a':
        print("É uma vogal.")
    case 'e':
        print("É uma vogal.")
    case 'i':
        print("É uma vogal.")
    case 'o':
        print("É uma vogal.")
    case 'u':
        print("É uma vogal.")
    case _:
        print("Não é uma vogal!")
