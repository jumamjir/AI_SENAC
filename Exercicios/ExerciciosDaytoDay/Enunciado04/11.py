# Exercício 11: Lista de Números Inteiros Positivos
# • Enunciado: Criar um programa com uma lista de 10 posições para guardar
# números inteiros positivos informados pelo usuário.
# • Estruturas Usar: while, if, input, print

numeros_positivos = []
contador = 0

while contador < 10:
    numero = int(input(f"Digite o número inteiro positivo {contador + 1}: "))
    if numero > 0:
        numeros_positivos.append(numero)
        contador += 1
    else:
        print("Por favor, digite um número inteiro positivo.")

print("Você digitou os seguintes números inteiros positivos:", numeros_positivos)
