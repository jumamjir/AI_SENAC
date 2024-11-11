# 23. Solicite ao usuário um nome de esporte (futebol, basquete, vôlei) e use
# match/case para exibir o número de jogadores em campo.

esporte = input("Digite o nome do esporte (futebol, basquete, vôlei): ").strip().lower()

match esporte:
    case "futebol":
        jogadores = 11
    case "basquete":
        jogadores = 5
    case "vôlei":
        jogadores = 6
    case _:
        print("Esporte não reconhecido. Tente novamente.")
        exit()

print(f"Número de jogadores em campo no {esporte}: {jogadores}")
