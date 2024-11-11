# 19. Solicite ao usuário um número que represente uma operação básica (1 = adição, 2
# = subtração, 3 = multiplicação, 4 = divisão) e dois números, usando match/case
# para realizar a operação.

operacao = int(input("Digite um número (1 = adição, 2 = subtração, 3 = multiplicação, 4 = divisão): "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

match operacao:
    case 1:
        resultado = num1 + num2
        print(f"A soma de {num1} e {num2} é: {resultado}")
    case 2:
        resultado = num1 - num2
        print(f"A subtração de {num1} e {num2} é: {resultado}")
    case 3:
        resultado = num1 * num2
        print(f"A multiplicação de {num1} e {num2} é: {resultado}")
    case 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"A divisão de {num1} por {num2} é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    case _:
        print("Operação inválida. Por favor, digite um número de 1 a 4.")
