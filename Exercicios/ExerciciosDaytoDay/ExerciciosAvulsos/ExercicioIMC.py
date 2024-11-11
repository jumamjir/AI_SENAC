#fazer um programa que ao informar o peso de 01 pessoa
#e verifique dentro da tabela do imc a classificação.
#mostrar o nome, peso e a classificação
nome = input("Informe o nome: ")
peso = float(input("Informe o peso: "))
altura = float(input("Informe a altura: "))

imc = peso/altura**2

print("O fulano: "+nome)

if imc <= 18.5:
    print("Abaixo do peso!")
elif imc <= 24.9:
    print("Peso bom")
elif imc <= 29.9:
    print("levemente acima do peso")
elif imc <= 34.9:
    print("Obsidade grau I")
elif imc <= 39.9:
    print("Obsidade grau II")
else:
    print("Obsidade grau III")