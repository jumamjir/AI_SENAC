# 14. Escreva um programa que leia uma lista de números e substitua todos os
# números negativos por zero.


lista = [3, -1, 4, -2, 5, -3]

for i in range(len(lista)):
    if lista[i] < 0:
        lista[i] = 0

print("Lista após substituição:", lista)
