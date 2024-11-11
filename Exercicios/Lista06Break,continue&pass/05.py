# 5. Leia uma frase e exiba as palavras, ignorando as palavras que contenham a letra
# "e" (continue).


lista = []

frase = input("Digite uma frase: ")

palavras = frase.split()

for palavra in palavras:
    if 'e' in palavra.lower():
        continue
    lista.append(palavra)

print(lista)

