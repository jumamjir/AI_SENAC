# 7. Escreva uma função que converta uma string para um número inteiro. Use
# tratamento de exceções para capturar erros de conversão.

def converte_string():
    try:
        frase = input("Digite uma frase: ")
        num = int(frase)
        print(type(num))
    except ValueError:
        print("Impossível de converter")


converte_string()