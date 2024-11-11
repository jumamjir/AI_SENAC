#27. Armazene as dimensões de um retângulo e exiba a área e perímetro.

print("Digite as medidas em centímetros.")
altura = int(input("Digite a medida da altura do retângulo:"))
base = int(input("Digite a medida da base do retângulo:"))

area = (base * altura)
perimetro = (base * 2) + (altura * 2)


print("A área deste retângulo é:",area, "cm²")
print("O perímetro deste retângulo é:",round(perimetro,2),"cm")