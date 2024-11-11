# Exercício 14: Lista de Números Pares
# • Enunciado: Criar um programa com uma lista de 10 posições para guardar
# números pares informados pelo usuário.
# • Estruturas Usar: while, if, input, print

numeros_pares = []
contador = 0

while contador < 10:
    numero = int(input(f"Digite o número par {contador + 1}: "))
    if numero % 2 == 0:
        numeros_pares.append(numero)
        contador += 1
    else:
        print("Por favor, digite um número par.")

print("Você digitou os seguintes números pares:", numeros_pares)
