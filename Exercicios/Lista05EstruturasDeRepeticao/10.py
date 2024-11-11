# 10.Solicite um número e exiba sua sequência Fibonacci até o número fornecido.
num = int(input("Digite um número: "))

a, b = 0, 1

print("Sequência de Fibonacci até", num, ":")

while a <= num:
    print(a, end=' ')
    a, b = b, a + b

print()

