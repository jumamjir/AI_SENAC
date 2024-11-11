# 15. Faça um programa que crie um dicionário com itens e preços e exiba o total a
# pagar por uma lista de compras fornecida pelo usuário.

itens = {
    "Maçã": 3.00,
    "Banana": 2.00,
    "Laranja": 4.00
}
total = 0
while True:
    item = input("Digite o nome do item (ou 'sair' para encerrar): ")
    if item.lower() == 'sair':
        break
    quantidade = int(input("Digite a quantidade: "))
    total += itens.get(item, 0) * quantidade
print(f"Total a pagar: R$ {total:.2f}")
