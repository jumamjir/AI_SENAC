# 14.Escreva um programa que solicite o preço de dois produtos e sugira qual é o mais
# barato.

preco1 = float(input("Digite um número:"))
preco2 = float(input("Digite um número:"))

if preco1 < preco2:
    print(f"{preco1} é mais barato que {preco2}")
else:
    print(f"{preco2} é mais barato que {preco1}")
