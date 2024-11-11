# 16. Crie uma função conta_palavras que receba uma frase e retorne o número de
# palavras na frase.


def conta_palavras(frase):
    separar = frase.split()
    return len(separar)

resultado = conta_palavras('ele joao pedro')
print(resultado)