#30. Leia um valor e use variável de conversão para exibir o valor em unidades de medida de comprimento.

num1 = float(input("Digite uma distância em metros:"))

centimetros = 100 * num1
milimetros = 1000 * num1
quilometros = 1000 / num1

print(num1,"metros")
print("O valor em centímetro é:",centimetros,"cm")
print("O valor em milímetro é:",milimetros,"mm")
print("O valor em quilômetros é:",quilometros,"km")

