LADO_A = 3
LADO_B = 4
LADO_C = 5
perimetro = LADO_A + LADO_B + LADO_C
s = perimetro / 2
area = (s * (s - LADO_A) * (s - LADO_B) * (s - LADO_C)) ** 0.5
print(f"Perímetro: {perimetro}, Área: {area:.2f}")
