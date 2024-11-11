def analisar_nome(nome):
    letras = len(nome.replace(" ", ""))
    palavras = len(nome.split())
    return letras, palavras

nome_completo = input("Digite seu nome completo: ")
letras, palavras = analisar_nome(nome_completo)
print(f"O nome completo contém {letras} letras e {palavras} palavras.")
