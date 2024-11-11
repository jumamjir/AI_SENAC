# 20. Escreva uma função eh_bissexto que receba um ano e retorne True se for um ano
# bissexto, e False caso contrário.


def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

resultado = eh_bissexto(2016)
print(resultado)