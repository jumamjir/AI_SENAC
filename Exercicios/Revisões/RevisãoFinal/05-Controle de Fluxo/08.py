peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))
IMC = peso / (altura ** 2)
if IMC < 18.5:
    classificacao = "leve"
elif 18.5 <= IMC < 24.9:
    classificacao = "normal"
elif 25 <= IMC < 29.9:
    classificacao = "acima do peso"
else:
    classificacao = "obesidade"
print(f"Classificação: {classificacao}")
