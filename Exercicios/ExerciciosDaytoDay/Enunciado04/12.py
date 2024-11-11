# Exercício 12: Lista de Números Inteiros Negativos
# • Enunciado: Criar um programa com uma lista de 10 posições para guardar
# números inteiros negativos informados pelo usuário.
# • Estruturas Usar: while, if, input, print

numeros_negativos = []
contador = 0

while contador < 10:
    numero = int(input(f"Digite o número inteiro negativo {contador + 1}: "))
    if numero < 0:
        numeros_negativos.append(numero)
        contador += 1
    else:
        print("Por favor, digite um número inteiro negativo.")

print("Você digitou os seguintes números inteiros negativos:", numeros_negativos)
