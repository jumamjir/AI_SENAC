# 5. Escreva um programa que leia uma lista de palavras e use for e if para contar
# quantas palavras começam com a letra a.

lista = ['Amanda','Joao','Pedro','Madeira']

contador = 0
for palavra in lista:
    if palavra.startswith('a') or palavra.startswith('A'):
        contador +=1


print("A quantidade de palavras que começam com a letra 'a':",contador )