# 2. Solicite ao usuário um símbolo matemático (+, -, *, /) e dois números; use
# match/case para realizar a operação indicada.


operacao = input("Digite um símbolo matemático (+, -, *, /): ")
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

match operacao:
    case '+':
        resultado = num1 + num2
        print(f"O resultado de {num1} + {num2} é: {resultado}")
    case '-':
        resultado = num1 - num2
        print(f"O resultado de {num1} - {num2} é: {resultado}")
    case '*':
        resultado = num1 * num2
        print(f"O resultado de {num1} * {num2} é: {resultado}")
    case '/':
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado de {num1} / {num2} é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    case _:
        print("Operação inválida. Por favor, use +, -, * ou /.")

