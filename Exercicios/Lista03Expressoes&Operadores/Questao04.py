#4.Solicite o peso e a altura de uma pessoa e calcule o IMC.
#formula IMC = divide-se o peso do paciente pela sua altura elevada ao quadrado

peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))

imc = peso / (altura**2)

print(round(imc,2))