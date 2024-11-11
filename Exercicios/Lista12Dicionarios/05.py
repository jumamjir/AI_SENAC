# 5. Escreva um programa que crie um dicionário com palavras e suas traduções e
# exiba a tradução de uma palavra fornecida pelo usuário.

dicionario = {
    "cachorro": "dog",
    "gato": "cat",
    "pássaro": "bird"
}
palavra = input("Digite uma palavra em português: ")
traducao = dicionario.get(palavra, "Tradução não encontrada.")
print(f"A tradução de '{palavra}' é: {traducao}")
