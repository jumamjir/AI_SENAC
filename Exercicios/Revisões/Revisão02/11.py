#11) criar um programa com lista de 10 posições para guardar números impares informados

lista = []
while len(lista) < 10:
    for i in range(1):
        num = int(input("Digite um número:"))
        if num % 2 == 1:
            lista.append(num)
            print("O número digitado é inteiro ímpar.")
        elif num % 2 == 0:
            print("O número digitado é inteiro par, digite um número ímpar!.")
            continue
        else:
            print("Número inválido")
            continue

print(lista)
print(len(lista))

