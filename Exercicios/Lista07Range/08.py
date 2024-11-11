# 8. Faça um programa que exiba os números de 1 a 10, excluindo o 5 usando range e
# continue.

for i in range(1,11):
    if i == 5:
        continue
    else:
        print(i)