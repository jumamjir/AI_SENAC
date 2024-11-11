#06-Pandas) Fazer um programa que leia 10870 valores e retorne o maior deles - OK

valorzao = 0

for i in range(5):
    valor = int(input("Digite um número:"))

    if valorzao == 0:
        valorzao = valor
    elif valor > valorzao:
        valorzao = valor

print("O maior valor é:", valorzao)
