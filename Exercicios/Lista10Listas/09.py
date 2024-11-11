# 9. Faça um programa que solicite ao usuário 10 números e exiba a lista em ordem
# decrescente.


lista = []

for i in range(10):
    num = int(input("Digite um número: "))
    lista.append(num)

listaInversa = []
while lista:
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    listaInversa.append(maior)
    lista.remove(maior)

print("Lista em ordem decrescente:", listaInversa)
