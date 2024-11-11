# 20. Crie um programa que solicite um idioma (inglês, espanhol, francês) e use
# match/case para exibir uma saudação básica nesse idioma.

idioma = input("Digite um idioma (inglês, espanhol, francês): ").strip().lower()

match idioma:
    case "inglês":
        print("Hello!")
    case "espanhol":
        print("¡Hola!")
    case "francês":
        print("Bonjour!")
    case _:
        print("Idioma não reconhecido. Por favor, escolha entre inglês, espanhol ou francês.")
