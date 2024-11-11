# 22. Escreva um programa que solicite ao usuário um formato geométrico (círculo,
# quadrado, triângulo) e use match/case para calcular a área correspondente.

forma = input("Digite o formato geométrico (círculo, quadrado, triângulo): ").strip().lower()

match forma:
    case "círculo":
        raio = float(input("Digite o raio do círculo: "))
        area = 3.14 * raio ** 2
    case "quadrado":
        lado = float(input("Digite o lado do quadrado: "))
        area = lado ** 2
    case "triângulo":
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        area = (base * altura) / 2
    case _:
        print("Formato não reconhecido. Tente novamente.")
        exit()

print(f"A área do {forma} é: {area}")
