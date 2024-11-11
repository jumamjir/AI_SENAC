#01) Desenvolva um programa que leia a idade de uma pessoa e exiba se ela é maior de
# idade (18 anos ou mais) ou menor de idade

num1 = int(input("Digite sua idade:"))

if num1 < 18:
    print("Você é menor de idade")
elif num1 >= 18:
    print("Você é maior de idade")
