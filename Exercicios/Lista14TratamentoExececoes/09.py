# 9. Faça uma função que abra um arquivo, leia seu conteúdo e exiba-o na tela.
# Capture exceções para arquivos inexistentes ou problemas de permissão de
# leitura.

nome_arquivo = input("Digite o nome do arquivo (com a extensão): ")

def abrir():
    try:
        arquivo = open(nome_arquivo, 'r')
        conteudo = arquivo.read()
        print(conteudo)
    except FileNotFoundError:
        print("Arquivo inexistente!")

    except PermissionError:
        print("Você não tem permissão para abrir este arquivo!")

    finally:
        if 'arquivo' in locals():
            arquivo.close()


abrir()
