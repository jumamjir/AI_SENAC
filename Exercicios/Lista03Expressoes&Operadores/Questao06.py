#6.Solicite um número e exiba seu valor absoluto e o negativo do número.

num1 = float(input("Digite um número:"))
absoluto = int(num1)
negativo = num1 * (-1)
print("Valor absoluto é =",absoluto)
print(f"O negativo de {num1} é = {negativo:.2f}")
