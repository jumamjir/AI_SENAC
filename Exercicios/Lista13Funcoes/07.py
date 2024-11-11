# 7. Crie uma função media que receba uma lista de números e retorne a média dos
# valores.


def media(lista = []):
    return sum(lista) / len(lista)

lista2 = [2,10]

resultado = media(lista2)

print(resultado)
