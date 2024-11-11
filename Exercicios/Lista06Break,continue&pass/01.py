# 1. Escreva um programa que leia números e interrompa quando o usuário digitar um
# número negativo (break).

while True:
    numero = int(input("Digite um número (ou um número negativo para sair): "))
    if numero < 0:
        print("Número negativo digitado. Saindo do programa.")
        break
    else:
        print(f"Número digitado: {numero}")
