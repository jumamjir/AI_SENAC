# Exercício 5: Multiplicar Elementos por um Valor
# o Enunciado: Multiplique todos os elementos de uma lista por um
# valor fornecido pelo usuário. A lista deve ser preenchida pelo
# usuário.
# o Estruturas Usar: while, if/else

lista = []
Verdade = True

while Verdade:
    num = float(input("Digite número que quer inserir na lista:"))
    lista.append(num)
    print(lista)
    sair = int(input("Digite 0 para sair, ou 1 para continuar:"))
    if sair == 0:
        Verdade = False
    elif sair == 1:
        continue
    else:
        print("Você digitou algo inválido.")

print(lista)
valor = float(input("Digite por qual valor deseja multiplicar os valores desta lista:"))

multiplicacao = []
for elemento in lista:
    multiplicacao.append(elemento * valor)

print(multiplicacao)