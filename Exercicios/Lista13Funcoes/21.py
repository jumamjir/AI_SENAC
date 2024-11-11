# 21. Faça uma função conta_caracter que receba uma string e um caractere e retorne
# quantas vezes o caractere aparece na string.

def conta_caracter(frase,a):
    frase = frase.lower()
    caractere = a
    return sum(frase.count(i) for i in caractere)


resultado = conta_caracter('AaaaLOUUUUU','a')
print(resultado)