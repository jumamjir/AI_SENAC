def aplicar_desconto(preco):
    desconto = preco * 0.15
    novo_preco = preco - desconto
    return novo_preco

preco = float(input("Digite o preço do produto: R$ "))
novo_preco = aplicar_desconto(preco)
print(f"O novo valor com desconto de 15% é: R$ {novo_preco:.2f}")
