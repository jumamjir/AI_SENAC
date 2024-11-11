#26. Solicite um valor inicial de depósito e uma constante de juros mensais para exibir o saldo previsto após um mês.

deposito = float(input("Digite o valor do depósito:"))
juros = 0.1
valorTotal = (deposito * juros) + deposito

print("O seu depósito após os juros totalizou em:$",valorTotal)
