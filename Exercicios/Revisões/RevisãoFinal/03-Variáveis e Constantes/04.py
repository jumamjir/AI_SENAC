preco_produto1 = float(input("Digite o preço do primeiro produto: "))
preco_produto2 = float(input("Digite o preço do segundo produto: "))
preco_produto3 = float(input("Digite o preço do terceiro produto: "))
TAXA_IMPOSTO = 0.15
valor_total = (preco_produto1 + preco_produto2 + preco_produto3) * (1 + TAXA_IMPOSTO)
print(f"Valor total com imposto: R$ {valor_total:.2f}")
