# 6.Solicite um número e exiba os números de 1 até o número fornecido.

num = int(input("Digite um número:"))

for i in range(1,num + 1):
    if num <= 1:
        print("Número errado")
    else:
        print(i)