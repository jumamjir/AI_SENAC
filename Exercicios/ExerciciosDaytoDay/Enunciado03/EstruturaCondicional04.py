# 4 - Faça um programa que leia um peso na Terra e o número de um planeta e mostre o valor do seu peso neste planeta.
# A relação de planetas é dada a seguir juntamente com o valor das gravidades relativas à Terra.

# Exercício de multiplas escolhas.

# 1 - 0,37 Mercúrio
# 2 - 0,88 Vênus
# 3 - 0,38 Marte
# 4 - 2,64 Júpiter
# 5 - 1,15 Saturno
# 6 - 1,17 Urano
#
# Para calcular o peso no planeta use a fórmula:
#
# (PlanetaTerra/10)*gravidade

pesoTerra = float(input("Digite uma medida de um peso:"))
print("Digite um número de um planeta: 1-Mercúrio,2-Vênus,3-Marte,4-Júpiter,5-Saturno,6-Urano")

gravidadePlanetas = float(input("Digite qual o planeta:"))

if (gravidadePlanetas == 1):
    gravidadePlanetas = 0.37
elif (gravidadePlanetas == 2):
    gravidadePlanetas = 0.88
elif (gravidadePlanetas == 3):
    gravidadePlanetas = 0.38
elif (gravidadePlanetas == 4):
    gravidadePlanetas = 2.64
elif (gravidadePlanetas == 5):
    gravidadePlanetas = 1.15
elif (gravidadePlanetas == 6):
    gravidadePlanetas = 1.17


formula = ((pesoTerra/10) * gravidadePlanetas)

print(f"O peso:{pesoTerra} será igual a: {formula} no planeta escolhido!")


