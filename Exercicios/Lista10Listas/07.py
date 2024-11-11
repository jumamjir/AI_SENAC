# 7. Crie uma lista de números e remova todos os elementos duplicados.

lista = [1,2,3,1,3,4,5,6,6,4,4,4,2,4,1]
numeros = []
for i in lista:
    if i not in numeros:
        numeros.append(i)
print(numeros)


