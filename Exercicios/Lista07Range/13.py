# 13. Use range para exibir os números de 0 a 10 em uma linha, separados por vírgulas.

for i in range(0, 11):
    if i == 0:
        print(i, end='')
    else:
        print(f", {i}", end='')

print()
