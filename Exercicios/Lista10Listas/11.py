# 11. Escreva um programa que leia uma lista de números e exiba o maior e o menor
# número.


lista = [1, 2, 3, 4, 5, 6, 7, 8, 15]
maior = lista[0]
menor = lista[0]
for i in lista:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(maior)
print(menor)
