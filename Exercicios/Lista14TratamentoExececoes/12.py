# 12. Faça um programa que execute uma operação aritmética fornecida pelo usuário
# (ex: 2 + 2) e trate exceções para operadores ou entradas inválidas.


try:
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite um outro número: "))
    ope = input("Digite a operação aritmética (+, -, *, /) ")

    if ope == '+':
        resul = num1 + num2
    elif ope == '-':
        resul = num1 - num2
    elif ope == '*':
        resul = num1 * num2
    elif ope == '/':
        if num2 == 0:
            raise ZeroDivisionError("Impossível dividir por 0")
        resul = num1 / num2
    else:
        raise ValueError("Operação Inválida")

    print("O resultado é ", resul)

except ValueError as e:
    print("Erro:", e)

except ZeroDivisionError as e:
    print("Erro:", e)
