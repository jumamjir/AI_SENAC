#12) criar um programa com lista de 10 posições para guardar números pares informados - OK


lista = []
while len(lista) < 3:
    for i in range(1):
        num = int(input("Digite um número:"))
        if num % 2 == 0:
            lista.append(num)
            print("O número digitado é inteiro par.")
        elif num % 2 == 1:
            print("O número digitado é inteiro ímpar, digite um número par!")
            continue
        else:
            print("Número inválido")
            continue

print(lista)
print(len(lista))
