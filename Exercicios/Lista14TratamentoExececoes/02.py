# 2. Crie uma função que leia um número inteiro do usuário. Se o usuário digitar algo
# que não é um número, capture a exceção e exiba uma mensagem de erro.

def numero():
    try:
        num1 = int(input("Digite um número inteiro: "))
        print(num1, "é um número!")
    except ValueError:
            print("O número digitado não é um número válido.")


numero()
