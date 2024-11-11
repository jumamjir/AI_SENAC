# 4. Escreva um programa que leia uma lista de números e interrompa a leitura se
# encontrar um número igual a zero (break).

lista = []
while True:
    numero = int(input("Digite um número (ou o número 0 para sair): "))
    if numero != 0:
        lista.append(numero)
    else:
        break

print(lista)