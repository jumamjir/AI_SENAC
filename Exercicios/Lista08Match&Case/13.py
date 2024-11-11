# 13. Solicite ao usuário uma nota musical (dó, ré, mi, etc.) e use match/case para exibir
# a frequência aproximada da nota em Hz.

nota = input("Digite uma nota musical (dó, ré, mi, fá, sol, lá, si): ").strip().lower()

match nota:
    case "dó":
        print("Frequência: 261.63 Hz")
    case "ré":
        print("Frequência: 293.66 Hz")
    case "mi":
        print("Frequência: 329.63 Hz")
    case "fá":
        print("Frequência: 349.23 Hz")
    case "sol":
        print("Frequência: 392.00 Hz")
    case "lá":
        print("Frequência: 440.00 Hz")
    case "si":
        print("Frequência: 493.88 Hz")
    case _:
        print("Nota não reconhecida.")
