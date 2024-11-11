# 7. Solicite números ao usuário e exiba-os até que ele digite 999 (break).
while True:
    num = int(input("Digite um número:"))
    if num == 999:
        break

    print(num)

