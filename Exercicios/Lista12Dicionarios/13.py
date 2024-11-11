# 13. Crie um dicionário com números de 1 a 10 e suas representações em palavras.
# Exiba a palavra correspondente a um número fornecido pelo usuário.

numeros_por_extenso = {
    1: "um",
    2: "dois",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",
    10: "dez"
}
numero = int(input("Digite um número de 1 a 10: "))
palavra = numeros_por_extenso.get(numero, "Número fora do intervalo.")
print(f"Representação por extenso: {palavra}")
