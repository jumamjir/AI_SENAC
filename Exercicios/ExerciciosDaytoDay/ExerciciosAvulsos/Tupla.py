def adicao():
    num = int(input("Digite um número:"))
    num1 = int(input("Digite outro número:"))
    soma = num + num1
    print(f"A soma entre {num} e {num1} é igual a:",soma)

def subtracao():
    num = int(input("Digite um número:"))
    num1 = int(input("Digite outro número:"))
    subtrair = num - num1
    print(f"A subtração entre {num} e {num1} é igual a:",subtrair)

def multiplicacao():
    num = int(input("Digite um número:"))
    num1 = int(input("Digite outro número:"))
    multiplicar = num * num1
    print(f"A multiplicação entre {num} e {num1} é igual a:",multiplicar)

def divisao():
    num = int(input("Digite um número:"))
    num1 = int(input("Digite outro número:"))
    dividir = (num / num1)
    print(f"A divisão entre {num} e {num1} é igual a:",dividir)

adicao()
subtracao()
multiplicacao()
divisao()
