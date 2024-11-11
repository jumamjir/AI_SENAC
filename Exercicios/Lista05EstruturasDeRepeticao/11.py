# 11.Faça um programa que leia 10 números e exiba quantos são pares e quantos são
# ímpares.

pares = []
impares = []
for i in range(10):
    num = int(input("Digite um número:"))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Os números pares são:",pares)
print("Os números ímpares são:",impares)
