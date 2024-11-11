#4-Um pitdog está precisando de um programa para mostrar o menu de seus x-saladas,
# utilizando a estrutura de múltiplas escolhas, seja criativo e faça.
#A saída será quando digitar 0. Pelo menos 6 tipos de x-saladas,3 refrigerantes e 2 sucos.

escolha = int(input("Escolha: 1-XBacon,2-XTudo,3-XFrango,4-XSimples,5-XRatão,6-XPodrão,\n"
"7-Guaraná,8-Coca-Cola,9-Mineiro,10-Suco de Maracujá,11-Suco de Laranja\n"
"Digite sua escolha:"))
Verdade = True
while escolha != 0:
    match escolha:
        case 0:
            break
        case 1:
            print("XBacon")
            break
        case 2:
            print("XTudo")
            break
        case 3:
            print("XFrango")
            break
        case 4:
            print("XSimples")
            break
        case 5:
            print("XRatão")
            break
        case 6:
            print("XPodrão")
            break
        case 7:
            print("Guaraná")
            break
        case 8:
            print("Coca-Cola")
            break
        case 9:
            print("Mineiro")
            break
        case 10:
            print("Suco de Maracujá")
            break
        case 11:
            print("Suco de Laranja")
            break