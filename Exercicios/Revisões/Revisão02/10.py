# 10) criar um programa com lista de 10 posições para guardar números inteiro negativos informados

lista = []
while len(lista) < 3:
    for i in range(3):
        num = int(input("Digite um número:"))
        if num < 0:
            lista.append(num)
        elif num >= 0:
            print("O número digitado não é inteiro negativo.")
            continue
        else:
            print("Número inválido")
            continue

print(lista)
