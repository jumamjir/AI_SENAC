# 1. Escreva um programa que leia uma lista de números e utilize um for para exibir se
# cada número é par ou ímpar usando if.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in lista:
    if i % 2 == 0:
        print(i, "é par!")
    else:
        print(i, "é ímpar!")
