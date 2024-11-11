# 8. Escreva um programa que leia uma lista de números e utilize for para somar todos
# os números. Se o número for negativo, use if para ignorá-lo e continue somando os
# positivos.

def somar_numeros():
    numeros = [10, -5, 8, 0, 3, -2, 7]  # Exemplo de lista de números
    soma = 0

    for numero in numeros:
        if numero < 0:
            continue
        soma += numero

    print(f'Soma dos números positivos: {soma}')

somar_numeros()
