# 8.Crie um programa que leia números até que o usuário digite zero, exibindo a soma
# dos números digitados.

lista = []


while True:
    num = int(input("Digite um número (ou 0 para sair):"))
    if num == 0:
        break
    else:
        lista.append(num)

soma = sum(lista)
print("A soma dos números:",soma)
