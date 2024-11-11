# Exercício 9: Lista de Números Inteiros
# • Enunciado: Criar um programa com uma lista de 10 posições para guardar
# números inteiros fornecidos pelo usuário.
# • Estruturas Usar: for, input, print

numeros = []

for i in range(10):
    numero = int(input(f"Digite o número inteiro {i + 1}: "))
    numeros.append(numero)

print("Você digitou os seguintes números:", numeros)
