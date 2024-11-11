#08-Matplotlib)Fazer um programa que leia o peso de 1344 pessoas e mostre a média de pesos


soma = 0
total = 1344
for i in range(total):
    peso = float(input("Digite seu peso: "))
    soma += peso
    media = (soma / total)

print("A soma dos pesos é:",soma)
print("A média dos pesos é:",media)