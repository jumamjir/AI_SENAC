#19. Defina uma constante para a taxa de imposto e calcule o valor total de um produto com esse imposto.


num1 = float(input("Digite o preço do produto:"))
imposto = 0.5
aumento = (num1 * imposto) + num1

print(f"O aumento do imposto mais o valor original do produto fez com que o preço total ficasse em:",aumento,"reais")
