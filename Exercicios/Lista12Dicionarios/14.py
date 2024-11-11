# 14. Escreva um programa que crie um dicionário com nomes de filmes e anos de
# lançamento e permita ao usuário buscar o ano de um filme específico.

filmes = {
    "Ação": 1994,
    "Titanic": 1997,
    "Matrix": 1999,
    "Avatar": 2009,
    "Inception": 2010
}
filme = input("Digite o nome de um filme: ")
ano = filmes.get(filme, "Filme não encontrado.")
print(f"Ano de lançamento de '{filme}': {ano}")
