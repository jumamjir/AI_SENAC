# 7.Leia uma lista de números e exiba apenas os números positivos.

lista = []


while True:
    num = int(input("Digite um número (ou 0 para sair):"))
    if num == 0:
        break
    elif num > 0:
        lista.append(num)

print("Números positivos:",lista)

