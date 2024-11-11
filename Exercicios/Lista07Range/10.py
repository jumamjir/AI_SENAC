# 10. Escreva um programa que use range para exibir os primeiros 10 números da
# sequência Fibonacci.

a, b = 0, 1

print("Os primeiros 10 números da sequência Fibonacci:")
for i in range(10):
    print(a)
    a, b = b, a + b
