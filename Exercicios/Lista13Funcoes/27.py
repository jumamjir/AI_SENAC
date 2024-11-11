# 27. Faça uma função calcula_raiz que receba um número e retorne sua raiz quadrada,
# considerando apenas números positivos.


def calcula_raiz(num1):
    if num1 > 0:
        return num1 ** (1/2)


resul = calcula_raiz(16)
print(resul)