# 3.Faça um programa que leia 5 números e exiba a soma deles.

lista = []
for i in range(5):
    num = int(input("Digite um número:"))
    lista.append(num)
soma = sum(lista)
print("A soma de todos os números é igual a:",soma)