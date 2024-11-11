# 8. Crie um programa que leia um número e calcule o logaritmo natural (log). Use
# tratamento de exceções para lidar com valores negativos e zero.

import math

try:
    num = float(input("Digite um número: "))

    if num <= 0:
        raise ValueError("O número deve ser maior que zero.")

    logaritmo = math.log(num)
    print(f"O logaritmo natural de {num} é: {logaritmo}")

except ValueError as e:
    print(e)
