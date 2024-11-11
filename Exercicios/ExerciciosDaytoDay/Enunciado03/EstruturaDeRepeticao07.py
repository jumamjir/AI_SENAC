#7 - Faça um programa com números que serão informados e
#mostre o triplo de cada número. O programa termina quando entrar o número -999.

Verdade = True
while Verdade:
    num = int(input("Digite um número:"))
    triplo = num * 3
    print(triplo)
    print("Caso queira parar, digite: '-999'")
    if num == -999:
        Verdade = False