# 11.Leia um número inteiro e exiba se ele é divisível por 3, 5, ambos ou nenhum.

num1 = int(input("Digite um número:"))

if num1 % 3 == 0 :
    print("É divisível por 3")
elif num1 % 5 == 0:
    print("É divisível por 5")
elif num1 % 3 == 0 and num1 % 5 == 0:
    print("É divisível por 3 e 5")
elif num1 % 3 != 0 and num1 % 5 != 0:
    print("Não é divisível por nenhum")
else:
    print("Inválido")









