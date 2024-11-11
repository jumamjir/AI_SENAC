num=int(input("informe o número: "))
#if simples
# if num < 0:
#     print("o número é negativo")
# else:
#     print("o número é positivo")

#if composto
# if num%2 == 0:
#     print("par")
# else:
#     print("impar")

#if composto
if num%3 == 0 and num%5==0:
    print("dividido pelos dois")
else:
    print("Não é dividido pelos dois")