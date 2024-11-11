#2-Faça um programa para verificar se um número é divisível por 3 e 9 ao mesmo tempo.

num = int(input("Digite um número divísel por 3 e 9 ao mesmo tempo:"))

if num % 3 == 0 and num % 9 == 0:
    print(num,"é divisível por 3 e 9.")
else:
    print("Não é divisível.")