#01) Fazer um programa que leia a idade de uma pessoa e informe se é maior de idade ou não

num1 = int(input("Digite sua idade:"))


if num1 < 18:
    print("Você é menor de idade!")

elif num1 >=18:
    print("Você é maior de idade!")