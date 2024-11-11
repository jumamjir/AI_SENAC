# 3. Faça um programa que leia um dicionário com produtos e preços e permita que o
# usuário adicione um novo produto com preço.

produtos = {}
while True:
    produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")
    if produto.lower() == 'sair':
        break
    preco = float(input("Digite o preço do produto: "))
    produtos[produto] = preco
print(produtos)
