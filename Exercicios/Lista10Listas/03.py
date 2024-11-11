# 3. Faça um programa que leia uma lista de números e exiba apenas os números
# pares.

lista = []
while True:
    num = int(input("Digite um número(ou 0 para sair): "))
    if num == 0:
        break
    elif num % 2 == 0:
        lista.append(num)
    else:
        print(num, "Não é par!")

print(lista)
