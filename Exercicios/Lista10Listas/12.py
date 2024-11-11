# 12. Faça um programa que leia uma lista de números e insira um zero após cada
# número par.

lista = [1, 2, 3, 4]

i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        lista.insert(i + 1, 0)
        i += 1
    i += 1

print("Lista modificada:", lista)

