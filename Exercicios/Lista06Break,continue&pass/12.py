# 12. Leia palavras até que uma palavra com mais de 10 caracteres seja inserida
# (break).

while True:
    nome = input("Digite um nome: ")

    if len(nome) >= 10:
        break

    print(nome)