# 13. Solicite números e exiba apenas os positivos, ignorando os negativos (continue).

numeros = []
while True:
    num = int(input("Digite um número (ou 0 para sair): "))
    if num % 2 != 0:
        continue
    elif num == 0:
        break
    else:
        numeros.append(num)

print(numeros)