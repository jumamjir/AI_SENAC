# 4. Crie um programa que solicite uma operação de potência (^) ou raiz quadrada (√)
# e um número, usando match/case para escolher qual operação executar.

import math

operacao = input("Digite uma operação (p para potência, rq para raiz quadrada): ")
numero = float(input("Digite um número: "))

match operacao:
    case 'p':
        expoente = float(input("Digite o expoente: "))
        resultado = numero ** expoente
        print(f"{numero} elevado a {expoente} é: {resultado}")
    case 'rq':
        if numero < 0:
            print("Erro: Não é possível calcular a raiz quadrada de um número negativo.")
        else:
            resultado = math.sqrt(numero)
            print(f"A raiz quadrada de {numero} é: {resultado}")
    case _:
        print("Operação inválida. Por favor, use p para potência ou rq para raiz quadrada.")
