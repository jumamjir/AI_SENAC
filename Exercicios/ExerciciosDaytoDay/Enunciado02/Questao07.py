# 07-NumPy) Fazer um programa que leia 20410 números e retorne a média entre o maior e o menor valor.

valorzao = 0
menorzao = 0
for i in range(2):
    valor = int(input("Digite sua idade: "))

    if valorzao == 0:
        valorzao = valor

    elif valor > valorzao:
        valorzao = valor

    elif valor < valorzao:
        menorzao = valor

media = (valorzao / menorzao)
print("A maior valor é:", valorzao)
print("O menor valor é:", menorzao)
print("A média é:", media)
