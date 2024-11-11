# Enunciado: Dada uma lista de números fornecida pelo usuário, conte quantos são pares e quantos são ímpares.

numeros = [int(x) for x in input("Digite números inteiros separados por espaço: ").split()]
pares = 0
impares = 0

for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Número de pares:", pares)
print("Número de ímpares:", impares)
