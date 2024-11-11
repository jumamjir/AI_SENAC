# #01) Faça um programa que leia 567 alturas e retorne a média das alturas.
# # Inicializa a lista para armazenar as alturas


alturas = []

for i in range(567):
    while True:
        try:
            altura = float(input(f"Digite a altura {i + 1} (em metros): "))
            if altura <= 0:
                print("A altura deve ser um valor positivo. Tente novamente.")
                continue

            sair = int(input("Digite 0 para sair ou 1 para continuar: "))
            if sair == 1:
                alturas.append(altura)
                break
            elif sair == 0:
                break
            else:
                print("Escolha inválida. Digite 0 para sair ou 1 para continuar.")

        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    if sair == 0:
        break

if alturas:
    media_alturas = sum(alturas) / len(alturas)
    print(f"A média das alturas é: {media_alturas:.2f} metros")
else:
    print("Nenhuma altura foi registrada.")

