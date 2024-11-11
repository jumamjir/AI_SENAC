# 9.Escreva um programa que leia a altura e o peso de uma pessoa e indique sua
# categoria de IMC (abaixo do peso, normal, sobrepeso, obesidade).

peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))

imc = peso / (altura**2)

print(round(imc,2))

if imc < 18.5:
    categoria = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    categoria = "Normal"
elif 25 <= imc < 29.9:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidade"

print(categoria)