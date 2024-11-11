

# Exercício 4: Imprimir Elementos de Índices Pares
# o Enunciado: Imprima todos os elementos que estão nos índices
# pares de uma lista.
# o Estruturas Usar: for, if/else



frutas = ["maçã", "banana", "laranja", "uva", "pera"]
for i in range(len(frutas)):
    if i % 2 == 0:
        print(frutas[i])
