#11. Leia um número em metros e converta para centímetros e milímetros

num = int(input("Digite uma metragem:"))
centimetros = 100 * num
milimetros = 1000 * num

print(num,"metros")
print("O valor em centímetro é:",centimetros,"cm")
print("O valor em milímetro é:",milimetros,"mm")
