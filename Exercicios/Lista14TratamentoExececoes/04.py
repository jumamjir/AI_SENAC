# 4. Escreva um programa que solicite ao usuário um índice de uma lista e exiba o
# valor correspondente. Utilize tratamento de exceções para lidar com índices fora
# do intervalo.


lista = ['agua','fogo','terra','ar']
print(lista)

try:
    indice = int(input("Qual o índice da lista que deseja acessar?"))
    valor = lista[indice]
    print(valor)
except ValueError:
    print("Número errado")

except IndexError:
    print("Índice fora do intervalo. A lista possui índices de 0 a", len(lista) - 1)