# 6. Faça um programa que leia uma lista de palavras e exiba a palavra mais longa.

lista = ['maça','uva','pera','abacate']
palavra_longa = ''
for i in lista:
    if len(i) > len(palavra_longa):
            palavra_longa = i

print(palavra_longa)