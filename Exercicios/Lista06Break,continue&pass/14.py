# 14. Escreva um programa que leia caracteres de uma string e use pass para
# caracteres especiais, processando apenas letras e números.

texto = input("Digite uma frase: ")

for char in texto:
    if char.isalnum():
        print(char)
    else:
        pass
