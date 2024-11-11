# 7. Crie um programa que peça ao usuário um número de 1 a 4 e use match/case para
# executar uma operação: 1 para soma, 2 para subtração, 3 para multiplicação e 4
# para divisão. Use if para validar a entrada.

def calculadora():
    operacao = int(input("Escolha uma operação (1: soma, 2: subtração, 3: multiplicação, 4: divisão): "))

    if operacao < 1 or operacao > 4:
        print("Entrada inválida. Por favor, escolha um número de 1 a 4.")
        return

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    match operacao:
        case 1:
            resultado = num1 + num2
            print(f'Resultado da soma: {resultado}')
        case 2:
            resultado = num1 - num2
            print(f'Resultado da subtração: {resultado}')
        case 3:
            resultado = num1 * num2
            print(f'Resultado da multiplicação: {resultado}')
        case 4:
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
            else:
                resultado = num1 / num2
                print(f'Resultado da divisão: {resultado}')

calculadora()
