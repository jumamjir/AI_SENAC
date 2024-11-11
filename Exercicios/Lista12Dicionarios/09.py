# 9. Faça um programa que crie um dicionário com produtos e seus estoques. Permita
# ao usuário consultar a quantidade em estoque de um produto.

estoque = {
    "Arroz": 50,
    "Feijão": 30,
    "Macarrão": 20
}
produto = input("Digite o nome do produto: ")
quantidade = estoque.get(produto, "Produto não encontrado.")
print(f"Quantidade em estoque de {produto}: {quantidade}")
