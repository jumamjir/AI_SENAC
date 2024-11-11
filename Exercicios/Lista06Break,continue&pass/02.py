# 2. Solicite ao usuário 10 números e exiba apenas os números pares usando
# continue.

numeros = []
for i in range(10):
    num = int(input("Digite um número: "))
    if num % 2 != 0:
        continue
    else:
        numeros.append(num)

print(numeros)