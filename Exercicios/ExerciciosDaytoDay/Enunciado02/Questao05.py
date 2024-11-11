#05-Controle de Fluxo) Fazer um programa que retorne a soma dos números pares de 0 a 10000

soma = 0

for i in range(5):
    numeros = int(input("Digite um número:"))
    if numeros % 2 == 0:
        soma += numeros
    else:
        continue

print("A soma dos números é igual a:",soma)