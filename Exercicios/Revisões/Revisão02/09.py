#09) criar um programa com lista de 10 posições para guardar números inteiro positivos informados


lista = []


for i in range(10):
    num = int(input("Digite um número:"))
    if num < 0:
        print("O número digitado não é inteiro positivo")
        continue
    elif num >= 0:
        lista.append(num)

print(lista)