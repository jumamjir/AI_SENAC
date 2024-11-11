# 9. Crie um programa que solicite ao usuário uma operação trigonométrica (seno,
# cosseno, tangente) e um ângulo; use match/case para calcular a operação usando
# o módulo math.

import math

operacao = input("Digite a operação trigonométrica (seno, cosseno, tangente): ").strip().lower()
angulo = float(input("Digite o ângulo em graus: "))

angulo_rad = math.radians(angulo)

match operacao:
    case "seno":
        resultado = math.sin(angulo_rad)
        print(f"O seno de {angulo} graus é: {resultado}")
    case "cosseno":
        resultado = math.cos(angulo_rad)
        print(f"O cosseno de {angulo} graus é: {resultado}")
    case "tangente":
        resultado = math.tan(angulo_rad)
        print(f"A tangente de {angulo} graus é: {resultado}")
    case _:
        print("Operação inválida. Por favor, use seno, cosseno ou tangente.")
