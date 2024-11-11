# 03-Variáveis e Constantes) Desenvolva um programa que leia dois valores numéricos e calcule e exiba tanto a média aritmética
# quanto a média ponderada, sendo o primeiro valor com peso de 30% e o segundo com peso de 70%.

num1 = int(input("Digite um valor:"))
num2 = int(input("Digite um valor:"))

mediAritmetica = (num1 + num2) / 2

mediaPonderada = ((num1 * 0.3) + (num2 * 0.7))

print(mediAritmetica)
print(mediaPonderada)
