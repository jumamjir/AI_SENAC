# 18. Escreva um programa que solicite o nome de um planeta e use match/case para
# exibir a posição dele no sistema solar.
planeta = input("Digite o nome de um planeta: ").strip().lower()

match planeta:
    case "mercúrio":
        print("Mercúrio é o 1º planeta do sistema solar.")
    case "vênus":
        print("Vênus é o 2º planeta do sistema solar.")
    case "terra":
        print("Terra é o 3º planeta do sistema solar.")
    case "marte":
        print("Marte é o 4º planeta do sistema solar.")
    case "júpiter":
        print("Júpiter é o 5º planeta do sistema solar.")
    case "saturno":
        print("Saturno é o 6º planeta do sistema solar.")
    case "urano":
        print("Urano é o 7º planeta do sistema solar.")
    case "netuno":
        print("Netuno é o 8º planeta do sistema solar.")
    case _:
        print("Planeta não reconhecido.")
