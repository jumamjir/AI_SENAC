# Enunciado: Encontre o maior e o menor número em uma lista de números inteiros. A lista terá que ser preenchida.

numeros = [int(x) for x in input("Digite números inteiros separados por espaço: ").split()]
maior = numeros[0]
menor = numeros[0]

for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print("O maior número é:", maior)
print("O menor número é:", menor)
