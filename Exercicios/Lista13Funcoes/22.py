# 22. Crie uma função gera_sequencia que receba dois números inteiros e retorne uma
# lista com os números no intervalo especificado.


def gera_sequencia(num1, num2):
    return list(range(num1, num2 + 1))


resultado = gera_sequencia(1, 3)
print(resultado)



