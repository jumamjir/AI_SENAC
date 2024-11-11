#07-NumPy) Fazer um programa que leia o valor de um produto e a condição de pagamento: se for a vista 10% de desconto ou
#a prazo com 15% de juros. O algoritmo deverá retornar o valor final do produto



num1 = int(input("Digite o valor do produto:"))
tipoPagamento = int(input("Digite 0 para à vista e 1 para pagar no crédito: "))

if tipoPagamento == 0:
    juros = 0.1
    valorConta = num1 - (num1 * juros)
    # valorFinal = num1 - valorConta
    print("O cliente pagou à vista e deverá pagar: R$",valorConta)
elif tipoPagamento == 1:
    juros = 0.15
    valorConta = (num1 * juros) + num1
    print("O cliente pagou no crédito e deverá pagar: R$",valorConta)