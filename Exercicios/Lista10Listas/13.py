# 13. Crie uma lista de compras e permita que o usuário adicione e remova itens da
# lista.

lista_compras = []

while True:
    acao = input("Digite 'adicionar', 'remover' ou 'sair': ").lower()

    if acao == 'adicionar':
        item = input("Item a ser adicionado: ")
        lista_compras.append(item)
    elif acao == 'remover':
        item = input("Item a ser removido: ")
        lista_compras.remove(item) if item in lista_compras else print("Item não encontrado.")
    elif acao == 'sair':
        break

print("Lista de compras:", lista_compras)

