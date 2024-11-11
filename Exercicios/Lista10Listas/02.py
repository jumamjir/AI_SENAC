# 2. Escreva um programa que solicite ao usuário 5 nomes e armazene-os em uma
# lista, exibindo a lista ao final.

lista = []
for i in range(5):
    nome = input("Digite um nome:")
    lista.append(nome)
print(lista)