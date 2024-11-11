# Exercício 10: Lista de Números Decimais
# • Enunciado: Criar um programa com uma lista de 10 posições para guardar
# números decimais fornecidos pelo usuário.
# • Estruturas Usar: for, input, print

numeros_decimais = []

for i in range(10):
    numero = float(input(f"Digite o número decimal {i + 1}: "))
    numeros_decimais.append(numero)

print("Você digitou os seguintes números decimais:", numeros_decimais)
