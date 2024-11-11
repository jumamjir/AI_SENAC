# 23. Escreva uma função soma_pares que receba uma lista de números e retorne a
# soma de todos os números pares da lista.


def soma_pares(lista):
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    return sum(pares)


resul = soma_pares([1,2,4])
print(resul)
