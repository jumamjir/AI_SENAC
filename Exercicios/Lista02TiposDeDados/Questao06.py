# #6. Solicite um nome completo e exiba a quantidade de caracteres em cada palavra

nome = input("Digite seu nome completo:")

palavras = nome.split()

contagem_caracteres = {palavra: len(palavra) for palavra in palavras}

for palavra in palavras:
 print(f"A palavra '{palavra}' tem {len(palavra)} caracteres.")
