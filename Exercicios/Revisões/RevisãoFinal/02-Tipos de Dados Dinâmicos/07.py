numeros = list(map(int, input("Digite uma lista de inteiros separados por espaço: ").split()))
impares = [num for num in numeros if num % 2 != 0]
print(impares)
