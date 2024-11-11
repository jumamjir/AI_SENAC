# 15.Crie um programa que leia 5 nomes e exiba-os em ordem reversa.

lista = []
for i in range(5):
    nome = input("Digite seu nome:")
    lista.append(nome)

print("Nomes em ordem reversa:")
for nome in reversed(lista):
    print(nome)