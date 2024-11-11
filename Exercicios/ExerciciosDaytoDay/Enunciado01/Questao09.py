#09) Fazer um programa que leia a quantidade de homens e mulheres que compareceram em uma festa e retorne
#qual teve maior quantidade e o percentual correspondente de cada um.

num1 = int(input("Digite quantos homens foram à festa:"))
num2 = int(input("Digite quantos mulheres foram à festa:"))

tipoH = "Homens"
tipoM = "Mulheres"

if num1 > num2:
    print(tipoH, "foram maioria na festa.")
elif num2 > num1:
    print(tipoM, "foram maioria na festa.")

total = num1 + num2

percentualH = (num1/total) * 100
percentualM = (num2/total) * 100

print(tipoH, "é equivalente a ",round(percentualH,2),"%")
print(tipoM, "é equivalente a ",round(percentualM,2),"%")
