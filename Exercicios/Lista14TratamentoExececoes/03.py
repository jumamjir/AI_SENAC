# 3. Faça um programa que leia um arquivo de texto fornecido pelo usuário. Use
# tratamento de exceções para exibir uma mensagem caso o arquivo não exista.

nome_arquivo = input("Digite o nome do arquivo (com a extensão): ")

try:
    arquivo = open(nome_arquivo, 'r')
    print(f"Arquivo {nome_arquivo} foi lido com sucesso!")
    conteudo = arquivo.read()
    print(conteudo)

except FileNotFoundError:
    print(f"O arquivo {nome_arquivo} não existe.")

finally:
    try:
        arquivo.close()
    except NameError:
        pass
