#3.Leia dois números e exiba qual deles é o maior, ou se são iguais.

num1 = int(input("Digite um número:"))
num2 = int(input("Digite um número:"))


if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num1 == num2:
    print("São iguais")
else:
    print(f"{num2} é maior que {num1}")