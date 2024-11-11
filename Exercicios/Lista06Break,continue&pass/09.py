# 9. Escreva um programa que leia nomes e pare quando o nome "fim" for digitado
# (break).


while True:
    nome = input("Digite um nome (digite 'fim' para sair): ")

    if nome.lower() == 'fim':
        break

    print(nome)

