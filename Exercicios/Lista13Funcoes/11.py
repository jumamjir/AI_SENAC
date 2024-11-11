# 11. Escreva uma função conta_vogais que receba uma string e retorne o número de
# vogais presentes na string.


def conta_vogais(frase):
    frase = frase.lower()
    vogais = 'aeiou'
    return sum(frase.count(i) for i in vogais)

resultado = conta_vogais('ALOUUUUU')
print(resultado)