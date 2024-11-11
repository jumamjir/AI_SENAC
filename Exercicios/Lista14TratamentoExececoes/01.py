# 1. Escreva um programa que solicite dois números do usuário e exiba o resultado da
# divisão entre eles. Use tratamento de exceção para evitar divisão por zero.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

try:
    num3 = (num1 / num2)
    print(num3)
except ZeroDivisionError:
    print("Digite um número válido diferente de 0.")