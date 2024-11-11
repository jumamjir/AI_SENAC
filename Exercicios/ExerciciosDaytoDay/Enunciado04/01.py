# Enunciado: Dada uma lista de números inteiros, some todos os elementos e exiba o resultado.

numeros = [int(x) for x in input("Digite números inteiros separados por espaço: ").split()]
soma = 0
for num in numeros:
    soma += num

print("A soma dos elementos da lista é:", soma)
