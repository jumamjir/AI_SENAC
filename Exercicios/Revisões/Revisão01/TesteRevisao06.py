# Calcule o montante de um capital de R$ 6.000,00, aplicado a
# juros compostos, durante 1 ano, à taxa de 3,5% ao mês.
#
#
# J = juros
# P = principal (capital)
# i = taxa de juros
# n = número de períodos

# J = P . i . n


capital = 6000.00
taxaJuros = 0.035
numPeriodo = 12
juros = capital * (1 + taxaJuros) ** numPeriodo

print("Os juros serão:$",round(juros,2))

