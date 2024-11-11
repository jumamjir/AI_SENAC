# Exercício 13: Lista de Números Ímpares
# • Enunciado: Criar um programa com uma lista de 10 posições para guardar
# números ímpares informados pelo usuário.
# • Estruturas Usar: while, if, input, print

numeros_impares = []
contador = 0

while contador < 10:
    numero = int(input(f"Digite o número ímpar {contador + 1}: "))
    if numero % 2 != 0:
        numeros_impares.append(numero)
        contador += 1
    else:
        print("Por favor, digite um número ímpar.")

print("Você digitou os seguintes números ímpares:", numeros_impares)
