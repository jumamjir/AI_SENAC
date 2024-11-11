# 5. Escreva um programa que solicite o nome de um polígono (triângulo, quadrado,
# pentágono, etc.) e exiba o número de lados usando match/case.
# Solicita ao usuário o nome de um polígono

poligono = input("Digite o nome de um polígono (triângulo, quadrado, pentágono, etc.): ").strip().lower()

match poligono:
    case "triangulo":
        print("Um triangulo tem 3 lados.")
    case "quadrado":
        print("Um quadrado tem 4 lados.")
    case "retangulo":
        print("Um retangulo tem 4 lados.")
    case "pentagono":
        print("Um pentágono tem 5 lados.")
    case "hexágono":
        print("Um hexágono tem 6 lados.")
    case _:
        print("Polígono não reconhecido. Tente outro.")
