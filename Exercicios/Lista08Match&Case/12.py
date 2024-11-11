# 12. Escreva um programa que leia o tipo de animal (cachorro, gato, pássaro) e exiba
# uma característica usando match/case.

animal = input("Digite o tipo de animal (cachorro, gato, pássaro): ").strip().lower()

match animal:
    case "cachorro":
        print("Cachorros são leais e amigáveis.")
    case "gato":
        print("Gatos são independentes e curiosos.")
    case "pássaro":
        print("Pássaros podem voar e têm penas.")
    case _:
        print("Animal não reconhecido.")
