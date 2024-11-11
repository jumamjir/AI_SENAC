#4. Leia o raio de um círculo e calcule a área e o perímetro.

raio = int(input("Digite o valor do raio:"))


pi = 3.14
diametro = 2 * raio
area = pi * (raio * raio)
perimetro = 2 * pi * raio


print("O diâmetro deste círculo é:",diametro, "cm")
print("A área deste círculo é:",area, "cm²")
print("O perímetro deste círculo é:",round(perimetro,2),"cm")
#perimetro = 2.pi.r