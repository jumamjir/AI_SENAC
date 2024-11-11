numero = int(input("Digite um número: "))
if numero % 2 == 0 and numero % 7 == 0:
    print("O número é divisível por 2 e 7.")
elif numero % 2 == 0:
    print("O número é divisível por 2.")
elif numero % 7 == 0:
    print("O número é divisível por 7.")
else:
    print("O número não é divisível por 2 nem por 7.")
