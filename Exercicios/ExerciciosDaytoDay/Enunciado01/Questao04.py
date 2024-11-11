#04-Expressões e Operadores) Fazer um programa que leia 3 valores e verifique se é possível formar triangulo (para formar
#triangulo nenhum valor pode ser maior que a soma dos demais)

num1 = int(input("Digite a medida do lado do triângulo:"))
num2 = int(input("Digite a medida do lado do triângulo:"))
num3 = int(input("Digite a medida do lado do triângulo:"))

def imprimePossivel():
    print("É possível formar triângulo.")
def imprimeImpossivel():
    print("Não é possível formar triângulo.")

if (num1 < (num2 + num3)) and (num2 < (num1 + num3)) and (num3 < (num1 + num2)):
    imprimePossivel()

elif (num1 > (num2 - num3)) and (num2 > (num1 - num3)) and (num3 > (num1 - num2)):
    imprimeImpossivel()
