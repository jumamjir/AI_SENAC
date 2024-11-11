#10. Leia um número em formato string e exiba-o formatado como moeda.

import locale

print(locale.setlocale(locale.LC_ALL, ''))

frase = (input("Digite o número: "))
print(type(frase))
FormatarFrase = float(frase)
print(locale.currency(FormatarFrase, grouping=True))