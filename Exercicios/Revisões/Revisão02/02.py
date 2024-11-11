#02-Tipos de Dados Dinâmicos) Desenvolva um programa que leia um valor numérico e verifique se ele é divisível por 5, por 8 ou por ambos.
# Exiba mensagens apropriadas para cada caso.


num1 = int(input("Digite um número:"))

if (num1 % 8 == 0) and (num1 % 5 == 0):
    print(num1, ", É divisível tanto por 5 quanto por 8.")
elif num1 % 5 == 0 :
    print(num1, ", É divisível por 5")
elif num1 % 8 == 0:
    print(num1, ", É divisível por 8")
else:
    print("Não é divisível por nenhum dos dois.")

