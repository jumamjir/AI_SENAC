# # 3. Faça um programa que leia uma lista de palavras e exiba apenas as que não
# # começam com a letra "a", usando continue.

lista = []

for i in range(3):
    frase = input("Digite uma palavra: ")
    if frase.lower().startswith('a'):
        continue
    else:
        lista.append(frase)
print(lista)

