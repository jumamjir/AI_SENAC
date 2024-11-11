# 10. Faça um programa que leia números e exiba apenas os múltiplos de 4, ignorando
# os demais (continue).

while True:
    num = int(input("Digite um número: "))

    if num % 4 == 0:
        print(num, "é múltiplo de 4!")
    else:
        continue