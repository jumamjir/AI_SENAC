# – Faça um programa com dicionários com nomes de 10 cores.

dicionario = {}
for i in range(10):
    cor1 = input("Informe um nome de uma cor:")
    dicionario[i] ={'Cor': cor1}


print(dicionario)