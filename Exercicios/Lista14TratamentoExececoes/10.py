# 10. Escreva um programa que solicite um valor numérico e converta para float.
# Capture exceções caso o valor digitado não seja numérico.


try:
    num = float(input("Digite um número: "))

except ValueError:
    print("Valor inválido")

