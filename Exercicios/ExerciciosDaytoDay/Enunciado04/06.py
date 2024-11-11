# Exercício 6: Contar Ocorrências de um Elemento
# o Enunciado: Conte quantas vezes um determinado elemento
# aparece em uma lista. O elemento será informado.
# o Estruturas Usar: for, if/else
# o A lista preenchida:
# lista = [1, 2, 2, 3, 4, 4, 4]
from itertools import count

lista = [1, 2, 2, 3, 4, 4, 4]

contagem = lista.count(1)
contagem2 = lista.count(2)
contagem3 = lista.count(3)
contagem4 = lista.count(4)


print(contagem)
print(contagem2)
print(contagem3)
print(contagem4)