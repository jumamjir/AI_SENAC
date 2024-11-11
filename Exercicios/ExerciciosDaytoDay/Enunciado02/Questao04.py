#04-Expressões e Operadores) Fazer um programa que leia a idade de 100 pessoas e retorne a média dessas idades -

soma = 0

for i in range(5):
    idade = int(input("Digite sua idade: "))

    soma += idade
    media = soma / idade


print("A soma das idades é:",soma)
print("A média das idades é:",media)