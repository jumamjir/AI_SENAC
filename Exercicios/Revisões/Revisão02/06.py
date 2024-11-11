#06-Pandas) Faça um programa que mostrar os números de 12 a 378 e quantos são pares e quantos são impares.


pares = []
impares = []

for i in range(12, 378):
    num = int(input("Digite um número:"))
    if num % 2 == 1:
        print(num, "é ímpar!")
        impares.append(num)
    else:
        print(num,"é par!")
        pares.append(num)


print(impares,"a quantidade de indíces é:",len(impares))
print(pares,"a quantidade de indíces é:",len(pares))
