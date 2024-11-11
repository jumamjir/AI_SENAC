# 02-Tipos de Dados Dinâmicos) Fazer um programa que leia 350 números e retorne a quantidade de números impares.

quantImpar = 0
for i in range(5):
    numero = int(input("Digite um número:"))
    if (numero % 2) == 1:
        quantImpar += 1

print("A quantidade de números ímpares é:",quantImpar)


