
num1 = float(input("Insira um numero: "))

num2 = float(input("Insira um numero: "))

num3 = float(input("Insira um numero: "))

if num1 < num2 and num1 < num3:
    soma_maiores = num2 + num3
elif num2 < num1 and num2 < num3:
    soma_maiores = num1 + num3
else:
    soma_maiores = num1 + num2


print("A soma dos  dois maiores numeros inseridos é")