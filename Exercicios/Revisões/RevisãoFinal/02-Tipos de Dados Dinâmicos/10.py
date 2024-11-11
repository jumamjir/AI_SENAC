arquivo = input("Digite o nome do arquivo com extensão: ")
nome_sem_extensao = arquivo.rsplit('.', 1)[0]
print(nome_sem_extensao)
