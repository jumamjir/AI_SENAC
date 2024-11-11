# 4. Crie um programa que solicite um número do usuário e, com um for, exiba a
# tabuada do número até 10. Utilize if para exibir uma mensagem especial quando o
# resultado for múltiplo de 5.

num = int(input("Digite um número: "))


for i in range(10):
    if i > 0:
        num = (i * 1) + i
    print(num)