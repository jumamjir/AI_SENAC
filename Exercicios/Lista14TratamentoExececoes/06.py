# 6. Faça um programa que solicite um número e divida 100 por esse número. Capture
# exceções para divisão por zero e erros de tipo (caso o usuário não digite um
# número).

try:
    num = int(input("Digite um número: "))
    numero = 100 / num
    print(numero)

except ZeroDivisionError:
    print("Não pode dividir por 0.")

except ValueError:
    print("Digite um número válido!")