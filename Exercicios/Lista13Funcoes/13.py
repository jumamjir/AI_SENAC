# 13. Crie uma função multiplica_lista que receba uma lista de números e um fator
# multiplicativo, retornando uma nova lista com os números multiplicados pelo
# fator.


def multiplica_lista(lista,num):
    lista2 = [x * num for x in lista]
    return lista2

resultado = multiplica_lista([1,2],3)
print(resultado)
