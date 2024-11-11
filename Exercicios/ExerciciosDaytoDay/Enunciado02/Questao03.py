# 03-Variáveis e Constantes) Fazer um programa que leia 200 números e retorne a soma dos valores divisíveis por 3 e 7 ao mesmo tempo
soma = 0

for i in range(5):
    num1 = int(input("Digite um número: "))



    if num1 % 3 == 0 and num1 % 7 == 0:
        soma += num1




print("A soma vai dar:",soma)