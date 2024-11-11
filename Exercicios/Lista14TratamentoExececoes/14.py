# 14. Crie um programa que solicite um número inteiro e calcule o fatorial, usando
# tratamento de exceção para números negativos.

def fatorial(n):
    if n < 0:
        raise ValueError("Não é possível calcular o fatorial de números negativos.")
    if n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

try:
    num = int(input("Digite um número inteiro: "))
    resultado_fatorial = fatorial(num)
    print(f"O fatorial de {num} é: {resultado_fatorial}")

except ValueError as e:
    print("Erro:", e)
