# 04-Expressões e Operadores) Desenvolva um programa que leia três valores numéricos distintos e exiba qual é o maior,
# o menor e o valor intermediário (o do meio).


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    maior = num1
    if num2 > num3:
        intermediario = num2
        menor = num3
    else:
        intermediario = num3
        menor = num2
elif num2 > num1 and num2 > num3:
    maior = num2
    if num1 > num3:
        intermediario = num1
        menor = num3
    else:
        intermediario = num3
        menor = num1
else:
    maior = num3
    if num1 > num2:
        intermediario = num1
        menor = num2
    else:
        intermediario = num2
        menor = num1

print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")
print(f"O valor intermediário é: {intermediario}")
