# 06-Pandas) Fazer um programa que leia o consumo médio em metros cúbicos de água de um cliente e o tipo de
# cliente (comercial R$ 2,84 o metro cúbico ou residencial R$ 2,68 o metro cúbico) O algoritmo deverá
# retornar o valor da conta.

num1 = int(input("Digite o valor gasto de água em metros cúbicos:"))
numCliente = int(input('Informe o tipo de cliente! Digite 0 para "comercial" ou 1 para "residencial": '))

if numCliente == 0:
    tarifa = 2.84
    valorConta = tarifa * num1
    print("O cliente é do tipo comercial e deverá pagar: R$",valorConta)
elif numCliente == 1:
      tarifa = 2.68
      valorConta = tarifa * num1
      print("O cliente é do tipo residencial e deverá pagar: R$", valorConta)
