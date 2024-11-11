# 26. Escreva uma função fatorial que receba um número inteiro e retorne o fatorial
# desse número.

def fatorial(num):
    if num < 0:
        return None
    resultado = 1
    while num > 1:
        resultado *= num
        num -= 1
    return resultado

print(fatorial(5))
print(fatorial(0))
print(fatorial(-3))
