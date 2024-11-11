# 18. Faça uma função calcula_desconto que receba o preço de um produto e um
# percentual de desconto e retorne o valor com o desconto aplicado.


def calcula_desconto(preco,desconto):
    return preco - (preco * (desconto/100))


resul = calcula_desconto(100,10)
print(resul)